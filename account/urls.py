from django.urls import path
from account import views

urlpatterns = [
    path('log', views.login, name='log'),
    path('reg', views.regist, name='reg'),
    path('logout',views.logout,name='logout')
]
