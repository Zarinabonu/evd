from django.urls import path, include
from rest_framework import views

from api.idea.views import idea_create

urlpatterns = [
    path('create/', idea_create.as_view(), name ='api-idea-create')

]