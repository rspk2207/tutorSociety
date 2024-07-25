from django.urls import path
from .views import RegisterView,LogoutView
from .serializer import CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

auth_urls = [
    path('register/', RegisterView.as_view(),name='register'),
    path('login/', CustomTokenObtainPairView.as_view(),name='jwt_token'),
    path('login/refresh/',TokenRefreshView.as_view(),name='jwt_refresh'),
    path('logout/',LogoutView.as_view(),name='logout')
]