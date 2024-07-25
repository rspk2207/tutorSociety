from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _
# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(_("Email Address"),unique=True,max_length=60)
    contact_no = models.CharField("Contact Number",max_length=10,default='')
    is_tutor = models.BooleanField("Student or Tutor",default=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username","password","first_name"]

    objects = CustomUserManager()

    def __str__(self):
        return self.username