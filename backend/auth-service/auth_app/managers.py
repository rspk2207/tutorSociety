from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    
    def create_user(self,email,username,password,first_name,**fields):
        if not email:
            raise ValueError("Email not specified")
        if not username:
            raise ValueError("Username not specified")
        if not first_name:
            raise ValueError("Username not specified")
        email = self.normalize_email(email)
        user = self.model(email=email,username=username,first_name=first_name,**fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,username,password,first_name,**fields):
        fields.setdefault("is_staff",True)
        fields.setdefault("is_superuser",True)
        fields.setdefault("is_active",True)
        if fields.get("is_staff") is not True:
            raise ValueError("is_staff should be true for superuser")
        if fields.get("is_superuser") is not True:
            raise ValueError("is_superuser should be true for superuser")        
        return self.create_user(email,username,password,first_name,**fields)