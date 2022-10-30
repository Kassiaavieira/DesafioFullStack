from django.contrib.auth.models import AbstractUser
from django.db import models


class Medico(AbstractUser):
    data_criacao = models.DateTimeField(auto_now_add=True)