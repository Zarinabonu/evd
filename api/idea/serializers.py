from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from Idea.models import Idea

class Idea_Serializer(ModelSerializer):
    class Meta:
        model = Idea
        fields = ('user', 'email', 'title', 'description')


