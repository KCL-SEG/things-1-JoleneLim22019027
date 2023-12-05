from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Thing(models.Model):
   name = models.TextField(max_length=30, unique=True, blank=False)
   description = models.TextField(max_length=120, unique=False, blank=True)
   quantity = models.IntegerField(
      validators=[
         MinValueValidator(0, message="Value must be greater than or equal to 0"),
         MaxValueValidator(100, message="Value must be lesser than or equal to 100")
      ]
   )
