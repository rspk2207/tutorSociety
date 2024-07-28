from django.urls import path
from .views import RegisterView,LogoutView,UpdateView
from .serializer import CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

auth_urls = [
    path('register', RegisterView.as_view(),name='register'),
    path('login', CustomTokenObtainPairView.as_view(),name='jwt_token'),
    path('login/refresh',TokenRefreshView.as_view(),name='jwt_refresh'),
    path('logout',LogoutView.as_view(),name='logout'),
    path('update/username',UpdateView.as_view(),name='update_username'),
    path('update/email',UpdateView.as_view(),name='update_email'),
    path('update/firstname',UpdateView.as_view(),name='update_firstname'),
    path('update/lastname',UpdateView.as_view(),name='update_lastname'),
    path('update/istutor',UpdateView.as_view(),name='update_istutor'),
    path('update/contact',UpdateView.as_view(),name='update_contact'),
    path('update/password',UpdateView.as_view(),name='update_password'),
]