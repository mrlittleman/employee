from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, 'home'),
]
