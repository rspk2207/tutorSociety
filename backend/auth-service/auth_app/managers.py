from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    
    def create_user(self,email,username,password,**fields):
        if not email:
            raise ValueError("Email not specified")
        if not username:
            raise ValueError("Username not specified")
        email = self.normalize_email(email)
        user = self.model(email=email,**fields)
        user.set_password(password)
        user.save()