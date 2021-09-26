from django.db import models

# Create your models here.
#catogery database
from django.urls import reverse


class categor(models.Model):
    name=models.CharField(max_length=100,unique=True)
    slug=models.CharField(max_length=100,unique=True)
    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'
    def get_url(self):
        return reverse('catview',args=[self.slug])
    def __str__(self):
        return '{}'.format(self.name)
# product datbase
class product(models.Model):
    name=models.CharField(max_length=100,unique=True)
    slug=models.CharField(max_length=100,unique=True)
    image=models.ImageField(upload_to='products')
    stock=models.IntegerField()
    price=models.IntegerField()
    available=models.BooleanField()
    des=models.CharField(max_length=2000)
    category=models.ForeignKey(categor,on_delete=models.CASCADE)
    def get_url(self):
        return reverse('itemdetail',args=[self.category,self.slug])
    def __str__(self):
        return '{}'.format(self.name)