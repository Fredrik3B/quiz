from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from json import dumps
from .serializer import QuizarkSerializer, QuestionSerializer, CheckAnswerSerializer
from .models import Quizark, Question
from accounts.models import Player


class QuizAPI(APIView):

    def get(self, request, quiz_id):
        quizark = Quizark.objects.get(playing_id=quiz_id)
        request.session["submitted_answers"] = 0
        request.session["question_count"] = quizark.question.all().count()
        request.session["submitted_answers"] = 0
        request.session["answered_id"] = []
        serializer = QuizarkSerializer(quizark, many=False)
        return Response(serializer.data)


    def post(self, request, quiz_id):
        try:
            player_hex = request.session["player"]
            player = Player.objects.get(uuid=player_hex)
        except Player.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        print("DATA:", request.data)

        serializer = CheckAnswerSerializer(data=request.data)
        if serializer.is_valid():
            player_answer = serializer.validated_data["answer"]
            question_id = serializer.validated_data["id"]

            if question_id in request.session["answered_id"]:
                return Response("Allerede svart", status=status.HTTP_200_OK)


            # Trenger Error handling
            right_answer = Question.objects.get(id=question_id).answer
            serializer.validated_data["answer"] = False

            request.session["answered_id"].append(question_id)
            request.session["submitted_answers"] += 1

            submitted_answers = request.session["submitted_answers"]
            question_count = request.session["question_count"]
            if submitted_answers == question_count:
                serializer.validated_data["finish"] = {"right_answers": player.right, "question_count": question_count}
                print("Deleted player")
                player.delete()

            if player_answer == right_answer:
                serializer.validated_data["answer"] = True
                # Score logic
                player.right += 1
                player.save()
                return Response(serializer.validated_data, status=status.HTTP_200_OK)
            return Response(serializer.validated_data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
