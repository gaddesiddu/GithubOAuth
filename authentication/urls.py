from django.contrib import admin
from django.urls import path,include
from authentication import views

urlpatterns = [
    path('',views.index,name="index"),
    path('accounts/profile/', views.profile, name='profile'), 
]
