from django.contrib import admin
from django.urls import path, include
from .import views


urlpatterns = [
    path('',views.index, name='index'),
    path('signup/',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    path('forget-password/',views.forget_password, name='forget-password'),
]