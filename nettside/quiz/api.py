from rest_framework.views import APIView
from .serializer import QuizarkSerializer


class QuizAPI(APIView):
    def get(self, request, id):
        Quizark.objects.get(id=id)
        serializer = QuizarkSerializer(profile, many=False)
        return Response(serializer.data)


    def post(self, request, id):
        try:
            player = request.user.player
        except player.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        print(request.data)

        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
