from rest_framework import serializers
from .models import *


class AnswerSerializers(serializers.Serializer):
    class Meta:
        model = Answer
        fields = ['__all__']


class QuestionSerializer(serializers.Serializer):
    answers = AnswerSerializers(read_only = True ,many=True)
    class Meta:
        model = Question
        fields = ['id','title','answers']


class QuizSerializer(serializers.Serializer):
    question = QuestionSerializer(read_only = True, many = True)
    class Meta:
        model = Quiz
        fields = ['id','title','question']

