from django.urls import path, include
from rest_framework import views

from api.user.views import Profile_Token_Create

urlpatterns = [
    path('token/', Profile_Token_Create.as_view(), name ='api-token-create')

]