# from datetime import datetime,timedelta
# import jwt
# from django.conf import settings
# from django.contrib.auth import get_user_model
# from rest_framework import authentication
# from ts_auth.settings import SECRET_KEY

# User = get_user_model()

# class JWTAuthentication(authentication.BaseAuthentication):
#     def authenticate(self,request):
#         jwt_header = request.META.get('HTTP_AUTHORIZATION')
        
#         if jwt_header is None:
#             return None
        
#         jwt_token = JWTAuthentication.get_token(jwt_header)

#         try:
#             payload = jwt.decode(jwt_token,SECRET_KEY,algorithm=['HS256'])
#         except jwt.exceptions.InvalidSignatureError:
#             raise rest_framework.exceptions.AuthenticationFailed('Invalid Signature')
#         except:
#             raise rest_framework.exceptions.ParseError()
        
#         email = payload.get('email')
#         if email is None:
#             raise rest_framework.exceptions.AuthenticationFailed('Email field missing in payload')
        
#         user = User.objects.filter(email=email).first()
#         if user is None:
#             raise rest_framework.exceptions.AuthenticationFailed('User not found')
        
#         return user,payload
    

#     def get_the_token_from_header(self, token):
#         token = token.replace('Bearer', '').replace(' ', '')
#         return token
    

#     def authentication_header(self,request):
#         return 'Bearer'
    

#     def create_jwt(self,user):
#         payload = {
#             'email': user.email,
#             'username': user.username,
#             'iat': datetime.now().timestamp(),
#             'exp': int((datetime.now()+timedelta(hours=10)).timestamp())
#         }
        
#         jwt_token = jwt.encode(payload,SECRET_KEY,algorithm='HS256')

#         return jwt_token