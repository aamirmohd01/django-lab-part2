from django.urls import path
from . import views

urlpatterns = [
    path('squares/<int:num1>/<int:num2>/', views.square_pairs, name='square_pairs'),
]
