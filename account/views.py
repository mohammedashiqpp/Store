from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.shortcuts import render, redirect
from account.models import *
from home.models import *
# Create your views here.
def login(reqeust):
    if reqeust.method=='POST':
        try:
            loged=regi.objects.get(username=reqeust.POST['username'],password=reqeust.POST['Password'])
            reqeust.session['username']=loged.username
            return redirect('homes')
        except regi.DoesNotExist:
             messages.info(reqeust,'invalid username and password')
        return render(reqeust,'register.html')
    return render(reqeust, 'register.html')
def regist(request):
    cat = categor.objects.all()
    if request.method=='POST':
        username=request.POST['Username']
        password=request.POST['Password']
        password2=request.POST['Password1']
        email=request.POST['Email']
        phone=request.POST['Phone']
        if password==password2:
            if regi.objects.filter(username=username).exists():
                messages.info(request,'user name already taken')
                return redirect('reg')
            elif regi.objects.filter(email=email).exists():
                messages.info(request,'email id already taken')
                return redirect('reg')
            else:
                user=regi.objects.create(username=username,password=password,email=email,phoneno=phone)
                user.save()
                return redirect('log')
        else:
            messages.info(request,'password does not mach')
            return redirect('reg')
    else:
        return render(request, 'register.html',{'cat':cat})

def logout(request):
    try:
        del request.session['username']
    except:
        return redirect('/')
    return redirect('/')


