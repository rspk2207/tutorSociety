from rest_framework.views import APIView
from django.http import HttpRequest
from .models import CustomUser
from .form import RegistrationForm
from django.views import View
import json
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken
from rest_framework import status
from rest_framework.response import Response
from .models import CustomUser


class RegisterView(APIView):
    
    def get(self,request) -> Response:
        return Response({'message':'Invalid request method GET'},status=status.HTTP_405_METHOD_NOT_ALLOWED)


    def post(self,request:HttpRequest) -> Response:
        try:       
            data = json.loads(request.body)

            form = RegistrationForm(data=data)

            if form.is_valid():
                user = CustomUser.objects.create_user(username=form.cleaned_data.get('username'),email=form.cleaned_data.get('email'),password=form.cleaned_data.get('password'),first_name=form.cleaned_data.get('first_name'))
                user.last_name = form.cleaned_data.get('last_name')
                user.contact_no = form.cleaned_data.get('contact_no')
                user.is_tutor = form.cleaned_data.get('is_tutor')
                user.save()
                
                return Response({'message':'Valid registration form received','data':form.cleaned_data},status=status.HTTP_200_OK)
            
            else:
                return Response({'message':'Registration form is not valid, please check with requirements once again','error':form.errors},status=status.HTTP_417_EXPECTATION_FAILED)
        
        except Exception:
            return Response({'message':'Some error occured'},status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):

    def get(self,request) -> Response:
        return Response({'message':'Invalid request method GET'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
    

    def post(self,request:HttpRequest) -> Response:
        try:
            bearer_token = request.META.get('HTTP_AUTHORIZATION')
            
            if bearer_token:
                data = json.loads(request.body)
                
                if 'refresh' in data:
                    refresh_token = data['refresh']
                    token = RefreshToken(refresh_token)
                    print(token)
                    token.blacklist()
                
                    return Response({'message':'Successfully logged out'},status=status.HTTP_205_RESET_CONTENT)
                
                else:
                    return Response({'message':'Failed to log out. Please provide refresh token'},status=status.HTTP_400_BAD_REQUEST)
            
            else:
                return Response({'message':'You are not logged in. Kindly log in to log out'},status=status.HTTP_401_UNAUTHORIZED)
        
        except Exception:
            return Response({'message':Exception},status=status.HTTP_400_BAD_REQUEST)
        


class UpdateView(APIView):

    def get(self,request) -> Response:
        return Response({'message':'Invalid request method GET'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
    

    def post(self,request:HttpRequest) -> Response:
        try:
            bearer_token = request.META.get('HTTP_AUTHORIZATION')
            
            if bearer_token:
                access_token = AccessToken(bearer_token.split()[1])
                payload = access_token.payload
                user = CustomUser.objects.get(id=payload.get('user_id'))
                data = json.loads(request.body)
                if request.path.endswith('username'):
                    user.username = data['username']
                    user.save()
                
                    return Response({'message':'Username updated successfully, new username is '+user.username},status=status.HTTP_200_OK)
                
                elif request.path.endswith('email'):
                    user.email = data['email']
                    user.save()
                
                    return Response({'message':'Email updated successfully, new email is '+user.email},status=status.HTTP_200_OK)                
                
                elif request.path.endswith('firstname'):
                    user.first_name = data['first_name']
                    user.save()
                
                    return Response({'message':'First name updated successfully, new first name is '+user.first_name},status=status.HTTP_200_OK)
                
                elif request.path.endswith('lastname'):
                    user.last_name = data['last_name']
                    user.save()
                
                    return Response({'message':'Last name updated successfully, new last name is '+user.last_name},status=status.HTTP_200_OK)
                
                elif request.path.endswith('istutor'):
                    user.is_tutor = data['is_tutor']
                    user.save()
                
                    return Response({'message':'Tutor field updated to '+user.is_tutor+' successfully'},status=status.HTTP_200_OK)
                
                elif request.path.endswith('contact'):
                    user.contact_no = data['contact_no']
                    user.save()
                
                    return Response({'message':'Contact number updated successfully, new contact number is '+user.contact_no},status=status.HTTP_200_OK)
                
                elif request.path.endswith('password'):
                    user.set_password(data['password'])
                    user.save()
                
                    return Response({'message':'password updated successfully'},status=status.HTTP_200_OK)
                                
                else:
                    return Response({'message':'Invalid url requested'},status=status.HTTP_404_NOT_FOUND)
            
            else:
                return Response({'message':'You are not logged in. Kindly log in to update profile'},status=status.HTTP_401_UNAUTHORIZED)
        
        except Exception as e:
            return Response({'message':str(e)},status=status.HTTP_400_BAD_REQUEST)


# class UpdateEmailView(View):

#     def get(self,request) -> Response:
#         return Response({'message':'Invalid request method GET'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
    

#     def post(self,request:HttpRequest) -> Response:
#         try:
#             bearer_token = request.META.get('HTTP_AUTHORIZATION')
#             if bearer_token:
#                 access_token = AccessToken(bearer_token.split()[1])
#                 payload = access_token.payload
#                 user = CustomUser.objects.get(id=payload.get('user_id'))
#                 user.email = request.body.email
#                 user.save()
#                 return Response({'message':'Username updated successfully, new username is '+user.username},status=status.HTTP_200_OK)
#             else:
#                 return Response({'message':'You are not logged in. Kindly log in to update email'},status=status.HTTP_401_UNAUTHORIZED)
#         except Exception:
#             return Response({'message':Exception},status=status.HTTP_400_BAD_REQUEST)


# class UpdateFirstNameView(View):

#     def get(self,request) -> Response:
#         return Response({'message':'Invalid request method GET'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
    

#     def post(self,request:HttpRequest) -> Response:
#         try:
#             bearer_token = request.META.get('HTTP_AUTHORIZATION')
#             if bearer_token:
#                 access_token = AccessToken(bearer_token.split()[1])
#                 payload = access_token.payload
#                 user = CustomUser.objects.get(id=payload.get('user_id'))
#                 user.first_name = request.body.first_name
#                 user.save()
#                 return Response({'message':'Username updated successfully, new username is '+user.username},status=status.HTTP_200_OK)
#             else:
#                 return Response({'message':'You are not logged in. Kindly log in to update email'},status=status.HTTP_401_UNAUTHORIZED)
#         except Exception:
#             return Response({'message':Exception},status=status.HTTP_400_BAD_REQUEST)


# class UpdateEmailView(View):

#     def get(self,request) -> Response:
#         return Response({'message':'Invalid request method GET'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
    

#     def post(self,request:HttpRequest) -> Response:
#         try:
#             bearer_token = request.META.get('HTTP_AUTHORIZATION')
#             if bearer_token:
#                 access_token = AccessToken(bearer_token.split()[1])
#                 payload = access_token.payload
#                 user = CustomUser.objects.get(id=payload.get('user_id'))
#                 user.email = request.body.email
#                 user.save()
#                 return Response({'message':'Username updated successfully, new username is '+user.username},status=status.HTTP_200_OK)
#             else:
#                 return Response({'message':'You are not logged in. Kindly log in to update email'},status=status.HTTP_401_UNAUTHORIZED)
#         except Exception:
#             return Response({'message':Exception},status=status.HTTP_400_BAD_REQUEST)
