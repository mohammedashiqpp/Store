from django.db import models
from account.models import *
# Create your models here.
class adress(models.Model):
    fullname=models.CharField(max_length=20)
    phoneno=models.IntegerField()
    landmark=models.SlugField()
    city=models.CharField(max_length=30)
    def __str__(self):
        return self.fullname

