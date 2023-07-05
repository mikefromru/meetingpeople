from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.conf import settings

from django.contrib.auth import get_user_model

from rest_framework import status

from django_filters.rest_framework import DjangoFilterBackend
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from django.core.mail import send_mail
import environ

env = environ.Env()
env.read_env()


# models
from .models import (
    Like
)

# serialisers
from .serializers import (
    SignupSerializer,
    LikeSerializer,
    UserListSerializer,
)

class SearchView(ListAPIView):

    permission_classes = [IsAuthenticated]
    queryset = get_user_model().objects.all()
    serializer_class = UserListSerializer
    filter_backends = [DjangoFilterBackend] 
    filterset_fields = ['gender', 'first_name', 'last_name', 'email'] # api/list?gender=M
    

class LikeView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        print(request.user.id)
        items = Like.objects.all()
        serializer = LikeSerializer(items, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        liked_user = int(request.data.get('liked_user'))
        obj_data = {'user': request.user.id, 'liked_user': liked_user}
        serializer = LikeSerializer(data=obj_data)

        if serializer.is_valid():

            # Проверить лайкал юзер другого юзера раньше или нет
            if Like.objects.filter(user=request.user.id, liked_user=liked_user).exists():
                return Response({'message': 'it exists already'})

            # Проверить чтобы не лайкал сам себя
            if request.user.id != liked_user:
                serializer.save()
                # Проверить на взаимную симпатию
                if Like.objects.filter(user=liked_user, liked_user=request.user.id).exists():
                    user_2 = get_user_model().objects.get(id=liked_user)
                    message1 = f'Вы понравились {user_2}! Почта участника: {user_2.email}.'
                    message2 = f'Вы понравились {request.user}! Почта участника: {request.user.email}.'
                    send_mail('MeetPpl', message1, env('EMAIL_HOST_USER'), [user_2.email])
                    send_mail('MeetPpl', message2, env('EMAIL_HOST_USER'), [request.user.email])
                return Response(serializer.data)
            return Response({'message': 'You can not like yourself'})
           
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SignupViewSet(mixins.CreateModelMixin,
                    viewsets.GenericViewSet):

    permission_classes = [AllowAny]
    serializer_class = SignupSerializer