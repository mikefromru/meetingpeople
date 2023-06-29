from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from rest_framework import status
from django.contrib.auth import authenticate, login

from .serializers import SignupSerializer


class SignupViewSet(mixins.CreateModelMixin,
                    viewsets.GenericViewSet):

    permission_classes = [AllowAny]
    serializer_class = SignupSerializer