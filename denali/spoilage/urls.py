from django.urls import path
from . import views

urlpatterns = [
    path('', views.spoilage_dashboard, name='spoilage_dashboard'),
]