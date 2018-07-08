from django.urls import path
from . import views

urlpatterns = [
    path('<int:itemId>/', views.item)
]