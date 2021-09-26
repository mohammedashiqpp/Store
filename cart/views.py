from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from home.models import *
from account.models import *
# Create your views here.
def checkout(reqeust,cite=None,tot=0,total=0,count=0,ser=15):

    try:
        ct=cartlist.objects.get(cart_id=cartsid(reqeust))
        cite = item.objects.filter(cart=ct,active=True)
        for i in cite:
            total += (i.proud.price * i.qulity)
            count += i.qulity
        if total > 0:
                tot = total + ser
        else:
            tot=0
    except ObjectDoesNotExist:
        pass
    return render(reqeust,'checkout.html',{'ci':cite,'tot':tot})
def cartsid(reqeust):
    #get section key
    cartid=reqeust.session.session_key
    #creation key
    if not cartid:
        cartid=reqeust.session.create()
    return cartid
def addcart(reqeust, prd_id, user=None):
    #products get
        adds=product.objects.get(id=prd_id)

        try:
            # call section to cart_id
            ct=cartlist.objects.get(cart_id=cartsid(reqeust))
        except cartlist.DoesNotExist:
            ct=cartlist.objects.create(cart_id=cartsid(reqeust))
            ct.save()
        try:
            citem=item.objects.get(proud=adds,cart=ct)
            if citem.qulity < citem.proud.stock:
                citem.qulity+=1
            citem.save()
        except item.DoesNotExist:
            citem=item.objects.create(proud=adds,qulity=1,cart=ct)
            citem.save()
        return redirect('cart')




def minusitem(request,prd_id):
    ct=cartlist.objects.get(cart_id=cartsid(request))
    prodt=get_object_or_404(product,id=prd_id)
    citem=item.objects.get(proud=prodt,cart=ct)
    if citem.qulity>1:
        citem.qulity-=1
        citem.save()
    else:
        citem.delete()
    return redirect('cart')
def deletes(request,prd_id):
    ct=cartlist.objects.get(cart_id=cartsid(request))
    prodt=get_object_or_404(product,id=prd_id)
    citem=item.objects.get(proud=prodt,cart=ct)
    citem.delete()
    return redirect('cart')
