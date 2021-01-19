from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializer import QuizarkSerializer, QuestionSerializer, CheckAnswerSerializer
from .models import Quizark


class QuizAPI(APIView):
    def get(self, request, quiz_id):
        quizark = Quizark.objects.get(playing_id=quiz_id)
        serializer = QuizarkSerializer(quizark, many=False)
        print(serializer.data)
        return Response(serializer.data)


    def post(self, request, quiz_id):
        try:
            player = request.session["player"]
        except player.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        print("DATA:", request.data)

        serializer = CheckAnswerSerializer(data=request.data)
        if serializer.is_valid():
             return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
