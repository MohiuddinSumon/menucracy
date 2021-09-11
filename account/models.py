from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from core.models import BaseModel


class UserType(models.TextChoices):
    ADMIN = 'ADMIN', _('Admin')
    EMPLOYEE = 'EMPLOYEE', _('Employee')
    OWNER = 'OWNER', _('Owner')


class User(AbstractUser, BaseModel):
    user_types = models.CharField(
        max_length=10,
        choices=UserType.choices,
        default=UserType.EMPLOYEE,
    )

