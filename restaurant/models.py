from django.db import models
import datetime

from django.core.exceptions import ValidationError

from account.models import User, UserType


class Restaurant(models.Model):
    name = models.TextField(unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='restaurants')

    def clean(self):
        if self.owner.user_types != UserType.OWNER:
            raise ValidationError({"owner": "only OWNER type users are allowed."})

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

