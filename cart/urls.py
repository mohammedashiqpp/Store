from django.urls import path

from cart import views
urlpatterns=[
    path('cart', views.checkout, name='cart'),
    path('add<int:prd_id>', views.addcart, name='addcart'),
    path('minus<int:prd_id>', views.minusitem, name='minusitem'),
    path('dlt/<int:prd_id>/', views.deletes, name='delete'),
]