from django.urls import path
from . import views

urlpatterns = [
    path('', views.adminpage),
    path('register', views.register),
    path('create', views.regchk),
    path('login', views.loginpage),
    path('logmein',views.loginchk),
    path('tags/new',views.tags),
    path('tags/create',views.mktags),
    path('zones/new',views.zones),
    path('zones/create',views.mkzones)
]