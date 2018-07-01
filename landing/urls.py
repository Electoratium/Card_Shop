from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'item', views.item, name='item'),
    url(r'^landing/', views.landing)
]