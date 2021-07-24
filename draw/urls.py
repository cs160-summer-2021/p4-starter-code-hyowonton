# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    path('phone', views.phone, name='phone'),
    path('shared', views.shared, name='shared'),
    path('submitted', views.submitted, name='submitted')
]
