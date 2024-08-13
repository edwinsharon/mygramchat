from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Feedpost(models.Model):
    feedimage=models.ImageField(upload_to='images/')
    description = models.CharField(max_length=300)
    User = models.ForeignKey(User, on_delete=models.CASCADE)