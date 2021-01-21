from rest_framework import serializers
from .models import Quizark, Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        exclude = ["answer"]

class QuizarkSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(many=True, read_only=True)
    class Meta:
        model = Quizark
        fields = ['title', 'question']

class CheckAnswerSerializer(serializers.ModelSerializer):
    # id = serializers.ReadOnlyField()
    id = serializers.IntegerField()
    class Meta:
        model = Question
        fields = ['id', 'answer']
