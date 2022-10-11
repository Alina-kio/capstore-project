from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class ConfirmCode(models.Model):
    code = models.CharField(max_length=8)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
