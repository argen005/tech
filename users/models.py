from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin



class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if email is None:
            raise TypeError('Users should be a Phone')
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        if password is None:
            raise TypeError('Password should be not None')
        if email is None:
            raise TypeError('Email should not be None')
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='Электронная почта', unique=True)
    phone = models.CharField(verbose_name='Номер телефона', max_length=255, unique=True, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    confirmation_code = models.CharField(verbose_name='Код подтверждения', max_length=6, null=True, blank=True)

    USERNAME_FIELD = 'email'
    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Список пользователей'

    def __str__(self):
        return str(self.email)


    def set_password(self, raw_password):
        return super().set_password(raw_password)