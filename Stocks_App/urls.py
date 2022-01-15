from django.contrib import admin
from django.urls import path

from Stocks_App import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='index'),
    path('query', views.query, name='query'),
    path('add', views.add, name='add'),
    path('buy', views.buy, name='buy'),
]
