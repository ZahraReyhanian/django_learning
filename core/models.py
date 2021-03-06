from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
  email = models.EmailField(unique=True)

  def __str__(self) -> str:
        return self.first_name + " " + self.last_name