from rest_framework import serializers
from .models import Quizark, Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question']

class QuizarkSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(many=True, read_only=True)
    class Meta:
        model = Quizark
        fields = ['title', 'question']

class CheckAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['answer']
