"""
Author: Abhishek
Description: This file is not a default file. We have to create this file for each django app.

"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^test/', views.test),
    url(r'^stocks/', views.get_stock_codes),
    url(r'^portfolio/add/', views.add_to_portfolio),
    url(r'^portfolio/get/', views.get_portfolio)
]

