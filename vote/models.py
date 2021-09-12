import datetime

from django.db import models

from restaurant.models import Menu
from account.models import User


class Vote(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="votes")
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="votes")
    day = models.DateField(default=datetime.date.today)

    def save(self, *args, **kwargs):
        self.menu.vote_count = self.menu.vote_count + 1
        self.menu.save()
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ("employee", "day")
