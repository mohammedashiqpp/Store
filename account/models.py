from django.db import models

# Create your models here.
# registraion database
class regi(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=10)
    email=models.EmailField()
    phoneno=models.IntegerField()
    def __str__(self):
        return self.username