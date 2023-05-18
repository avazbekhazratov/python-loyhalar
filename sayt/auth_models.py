from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models


class Boshqaruvchi(UserManager):
    def create_user(self, username, password=None, is_staff=False, is_superuser=False, is_active=True, **extra_fields):
        user = self.model(
            username=username,
            password=password,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
            **extra_fields
        )

        user.set_password(str(password))
        user.save()
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        return self.create_user(username, password, True, True)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=128, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    oferta = models.BooleanField(default=True)

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = Boshqaruvchi()

    USERNAME_FIELD = 'username'
