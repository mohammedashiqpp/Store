from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render, get_object_or_404, redirect
from . models import *
from cart.models import *
from account.models import *
# Create your views here.
def homes(request,slugs=None):
    #catagory calling url code
    category_page=None
    prdt=None
    if slugs!=None:
        category_page=get_object_or_404(categor,slug=slugs)
        prdt=product.objects.filter(category=category_page,available=True)
    else:
        prdt=product.objects.all().filter(available=True)
    cat=categor.objects.all()
    #paginator call
    paginator = Paginator(prdt, 6)
    try:
        page = int(request.GET.get('page', 1))
    except:
        page = 1
    try:
        pro = paginator.page(page)
    except(EmptyPage, InvalidPage):
        pro = paginator.page(paginator.num_pages)


    return render(request,'index.html',{'cat':cat,'prd':prdt,'pg':pro})
def allproduct(request, slugs=None):
    category_page = None
    prdt = None
    if slugs != None:
        category_page = get_object_or_404(categor, slug=slugs)
        prdt = product.objects.filter(category=category_page, available=True)
    else:
        prdt = product.objects.all().filter(available=True)
    cat = categor.objects.all()

    c_page = get_object_or_404(categor, slug='FrozenFood')
    c_page1 = get_object_or_404(categor, slug='Beverages')
    c_page2 = get_object_or_404(categor, slug='Breadbakery')
    c_page3 = get_object_or_404(categor, slug='Vegitable')
    c_page4 = get_object_or_404(categor, slug='PetFood')
    c_page5 = get_object_or_404(categor, slug='Fruits')
    c_page6 = get_object_or_404(categor, slug='Households')
    c_page7 = get_object_or_404(categor, slug='Kitchen')

    prd = product.objects.filter(category=c_page, available=True)
    prd1 = product.objects.filter(category=c_page1, available=True)
    prd2 = product.objects.filter(category=c_page2, available=True)
    prd3 = product.objects.filter(category=c_page3, available=True)
    prd4= product.objects.filter(category=c_page4, available=True)
    prd5 = product.objects.filter(category=c_page5, available=True)
    prd6 = product.objects.filter(category=c_page6, available=True)
    prd7 = product.objects.filter(category=c_page7, available=True)
    paginator = Paginator(prd, 4)
    paginator1 = Paginator(prd1, 4)
    paginator2 = Paginator(prd2, 4)
    paginator3 = Paginator(prd3, 4)
    paginator4 = Paginator(prd4, 4)
    paginator5 = Paginator(prd5, 4)
    paginator6 = Paginator(prd6, 4)
    paginator7 = Paginator(prd7, 4)
    try:
        page = int(request.GET.get('page', 1))
    except:
        page = 1
    try:
        pro = paginator.page(page)
        pro1 = paginator1.page(page)
        pro2 = paginator2.page(page)
        pro3 = paginator3.page(page)
        pro4 = paginator4.page(page)
        pro5 = paginator5.page(page)
        pro6 = paginator6.page(page)
        pro7 = paginator7.page(page)


    except(EmptyPage, InvalidPage):
        pro = paginator.page(paginator.num_pages)
        pro1 = paginator1.page(paginator.num_pages)
        pro2 = paginator2.page(paginator.num_pages)
        pro3 = paginator3.page(paginator.num_pages)
        pro4 = paginator4.page(paginator.num_pages)
        pro5 = paginator5.page(paginator.num_pages)
        pro6 = paginator6.page(paginator.num_pages)
        pro7 = paginator7.page(paginator.num_pages)
    return render(request,'products.html',{
        'cat':cat,
        'prd':prd,
        'prd1':prd1,
        'prd2':prd2,
        'prd3':prd3,
        'prd4':prd4,
        'prd5':prd5,
        'prd6':prd6,
        'prd7':prd7,
        'pro':pro,
        'pro1': pro1,
        'pro2': pro2,
        'pro3': pro3,
        'pro4': pro4,
        'pro5': pro5,
        'pro6': pro6,
        'pro7': pro7,
    })
def itemdetails(request,slugs,productslugs):
    try:
        products=product.objects.get(category__slug=slugs,slug=productslugs)
    except Exception as e:
        raise e

    return render(request,'single.html',{'pr':products})
def contact(request):
    cat = categor.objects.all()
    return render(request,'mail.html',{'cat':cat})
def contact(request):
    cat = categor.objects.all()
    return render(request,'about.html',{'cat':cat})