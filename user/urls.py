from django.urls import path
from . import views

urlpatterns = [
    path('listusers/', views.listusers, name='listusers'),
    path('userhome/', views.userhome, name='userhome'),
    path('adduser/', views.adduser, name='adduser'),
    path('adduser_success/', views.adduser_success, name='adduser_success'),
]

