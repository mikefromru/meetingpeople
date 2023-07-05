from django.urls import path
from .views import SignupViewSet, LikeView, SearchView
from rest_framework.authtoken import views


urlpatterns = [
    path('api/clients/create/', SignupViewSet.as_view({'post': 'create'})),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/clients/like/', LikeView.as_view()),
    path('api/list/', SearchView.as_view(), name='search'),
    # path('api/clients/<int:id>/match/', LikeView.as_view()),
]

