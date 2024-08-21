# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('parking_info/', views.parking_info, name='parking_info'),
]