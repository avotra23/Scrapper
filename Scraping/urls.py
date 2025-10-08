"""
URL configuration for SCRAPPER project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Scraping.views import *

urlpatterns = [
    path('',home,name="home"),
    path('test/',test,name="test"),
    path('traiter_url/',traiter_url, name="traiter_url"),
    path('traiter_url1/',traiter_url1, name="traiter_url1"),
    path('traiter_url2/',traiter_url, name="traiter_url2"),
    path('traiter_url3/',traiter_url, name="traiter_url3"),
    path('traiter_url4/',traiter_url, name="traiter_url4"),
    path('traiter_url5/',traiter_url, name="traiter_url5"),
]
