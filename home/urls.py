from django.urls import path
from home import views
urlpatterns=[

    path('product',views.allproduct,name='product'),
    path('<slug:slugs>/', views.homes, name='catview'),
    path('<slug:slugs>/<slug:productslugs>',views.itemdetails, name='itemdetail'),
    path('contact',views.contact,name='contact'),
    path('about',views.contact,name='about'),

    path('',views.homes,name='homes'),

]