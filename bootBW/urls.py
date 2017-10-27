"""bootBW URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from homepage import views

urlpatterns = [
    url(r'^contact', views.contact, name='contact'),
    url(r'^case', views.case, name='case'),
    url(r'^case_show', views.case_show, name='case_show'),
    url(r'^about', views.about, name='about'),
    url(r'^admin', admin.site.urls, name='admin'),
    url(r'^index', views.index, name='index'),
    url(r'^$', views.index, name='index_default'),
]
