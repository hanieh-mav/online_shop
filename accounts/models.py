from django.shortcuts import reverse
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManger

# Create your models here.
class User(AbstractBaseUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200,unique=True)
    phone = models.CharField(max_length=12)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_shopadmin = models.BooleanField(default=False)

    objects = UserManger()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','phone']

    class Meta:
        ordering = ['-is_admin','-is_shopadmin']

    def __str__(self):
        return self.first_name

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_lable):
        return True

    @property
    def is_staff(self):
        return self.is_admin            


    def get_absolute_url(self):
        return reverse('dashboard:user-list')