from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('login/sign-up/', views.sign, name="sign-up"),
    path('logout/', views.logout, name="logout"),
    path('myaccount/', views.account, name="myaccount")
]