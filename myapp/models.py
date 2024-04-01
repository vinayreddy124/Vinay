from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        USER = 'USER', 'User'
        DEALER = 'DEALER', 'Dealer'

    role = models.CharField(max_length=50, choices=Role.choices)

    def _str_(self):
        return self.username
