from django.urls import path
from . import views

urlpatterns = [
    path('', views.repricing, name='repricing'),
]