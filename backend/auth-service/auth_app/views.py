from typing import Any
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from .models import CustomUser
from .form import RegistrationForm
from django.views import View
import json
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
# from .serializer
class RegisterView(View):
    
    def get(self,request) -> JsonResponse:
        return JsonResponse({'message':'Invalid request method GET'})


    def post(self,request:HttpRequest) -> JsonResponse:
        try:       
            data = json.loads(request.body)

            form = RegistrationForm(data=data)

            if form.is_valid():
                user = CustomUser.objects.create_user(username=form.cleaned_data.get('username'),email=form.cleaned_data.get('email'),password=form.cleaned_data.get('password'),first_name=form.cleaned_data.get('first_name'))
                user.last_name = form.cleaned_data.get('last_name')
                user.contact_no = form.cleaned_data.get('contact_no')
                user.is_tutor = form.cleaned_data.get('is_tutor')
                user.save()
                return JsonResponse({'message':'Registration form is working','data':form.cleaned_data})
            else:
                return JsonResponse({'message':'Registration form is not working lmao','error':form.errors})
        except Exception:
            return {'message':'Some error occured'}

class LogoutView(View):

    def get(self,request) -> JsonResponse:
        return JsonResponse({'message':'Invalid request method GET'})
    

    def post(self,request:HttpRequest) -> JsonResponse:
        try:
            data = json.loads(request.body)
            if 'refresh' in data:
                refresh_token = data['refresh']
                token = RefreshToken(refresh_token)
                print(token)
                token.blacklist()
                return JsonResponse({'message':'Successfully logged out'},status=status.HTTP_205_RESET_CONTENT)
            else:
                return JsonResponse({'message':'Failed to log out'},status=status.HTTP_400_BAD_REQUEST)

        except Exception:
            return JsonResponse({'message':Exception},status=status.HTTP_400_BAD_REQUEST)
        
        