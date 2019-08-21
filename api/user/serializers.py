from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from User.models import Register_profile


class Profile_Serializer(ModelSerializer):
    phone = serializers.CharField(required=False)
    key = serializers.CharField(required=False)
    class Meta:
        model = Token
        fields = ('phone', 'key')

    def create(self, validated_data):
        r =Register_profile(**validated_data)
        request = self.context['request']
        phone = request.data['phone']
        u,s = User.objects.get_or_create(username=phone)
        token, _ = Token.objects.get_or_create(user=u)
        print('USER:',token)

        return token







