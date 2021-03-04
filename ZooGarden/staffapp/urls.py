from django.urls import path
from . import views

urlpatterns = [
    path('', views.adminpage),
    path('register', views.register),
    path('create', views.regchk),
    path('login', views.loginpage),
    path('logmein',views.loginchk),
]