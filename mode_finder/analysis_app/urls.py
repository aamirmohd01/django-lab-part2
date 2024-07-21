from django.urls import path
from . import views

urlpatterns = [
    path('mode/<str:numbers>/', views.find_mode, name='find_mode'),
]
