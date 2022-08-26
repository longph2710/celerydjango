from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_number),
    path('mul/', views.mul_number),
    path('backup/', views.perform_backup)
]