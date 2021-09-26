from django.db import models
from account.models import *
from home.models import *
# Create your models here.
# cartlist db
class cartlist(models.Model):
    cart_id=models.CharField(max_length=200,unique=True)
    cart_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.cart_id
class item(models.Model):
    proud=models.ForeignKey(product,on_delete=models.CASCADE)
    cart =models.ForeignKey(cartlist,on_delete=models.CASCADE)
    qulity=models.IntegerField()
    active=models.BooleanField(default=True)
    def __str__(self):
        return self.proud
    def total(self):
        return self.proud.price * self.qulity

    def tot(self):
        ser = 15
        return self.proud.price * self.qulity + ser
