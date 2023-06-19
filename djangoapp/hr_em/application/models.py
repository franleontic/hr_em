from django.db import models
from django.contrib.auth.models import User
import numpy as np

class Text(models.Model):
    text = models.CharField(max_length=2000)
    rating = models.BinaryField()
    rating_list = models.BinaryField()
    dim = models.BooleanField()
    confidence = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

