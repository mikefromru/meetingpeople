from django.urls import path
from .views import SignupViewSet
from rest_framework.authtoken import views


urlpatterns = [
    path('api/clients/create/', SignupViewSet.as_view({'post': 'create'})),
    path('api-token-auth/', views.obtain_auth_token),
]

