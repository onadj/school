# education/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('exercises/', views.exercises, name='exercises'),
]
