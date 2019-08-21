from django.http import HttpResponse
from rest_framework import status
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import Idea_Serializer
from Idea.models import Idea

class idea_create(CreateAPIView):
    queryset = Idea.objects.all()
    serializer_class = Idea_Serializer
