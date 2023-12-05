from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Thing(models.Model):
   name = models.TextField(max_length=30, unique=True, blank=False)
   description = models.TextField(max_length=120, unique=False, blank=True)
   quantity = models.IntegerField(
      validators=[
         MinValueValidator(0),
         MaxValueValidator(100)
      ]
   )
