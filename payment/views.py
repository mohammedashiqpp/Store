from django.shortcuts import render, redirect
from .models import adress
from account.models import regi
from account.views import *
from account.views import login
# Create your views here.
def payment(request, user=None):
    if request.method=='POST':

            fullname = request.POST['name']
            phoneno = request.POST['phoneno']
            landmark = request.POST['landmark']
            city = request.POST['city']
            adr=adress.objects.create(fullname=fullname,phoneno=phoneno,landmark=landmark,city=city)
            adr.save()
            return redirect('payment')




    return render(request,'payment.html')
