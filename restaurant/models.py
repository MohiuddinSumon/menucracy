from django.core.validators import MinValueValidator
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


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menus')
    name = models.CharField(null=False, max_length=60)
    details = models.TextField(null=True, blank=True)
    serving_date = models.DateField(default=datetime.date.today)
    vote_count = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])

    class Meta:
        unique_together = ("restaurant", "serving_date")

    def __str__(self):
        return f'Menu = {self.name}, Vote = {self.vote_count}'
