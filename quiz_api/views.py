from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *


# Create your views here.

class QuizViewset(viewsets.ModelViewSet):
    queryset =  Quiz.objects.all()
    serializer_class = QuizSerializer





