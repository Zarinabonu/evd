from _contextvars import Token

from django.contrib.auth import authenticate
from pytz import unicode
from rest_framework import generics, permissions, status, request
from rest_framework.decorators import permission_classes
from rest_framework.generics import CreateAPIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from User.models import Register_profile
from rest_framework.response import Response
from .serializers import Profile_Serializer
from django.contrib.auth.models import User


@permission_classes((AllowAny,))
class Profile_Token_Create(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = Profile_Serializer



