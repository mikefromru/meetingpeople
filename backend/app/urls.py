from django.urls import path
from .views import SignupViewSet, LikeView
from rest_framework.authtoken import views


urlpatterns = [
    path('api/clients/create/', SignupViewSet.as_view({'post': 'create'})),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/clients/like/', LikeView.as_view()),
    # path('api/clients/<int:id>/match/', LikeView.as_view()),
]

