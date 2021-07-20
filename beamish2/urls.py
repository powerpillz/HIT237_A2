"""beamish2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from beamish2_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #Home Page
    url(r'^$', views.Home, name='Home'),

    #Mine Site pages
    url(r'^list[m,M]ines/?$', views.listMines, name='listMines'),
    url(r'^add[m,M]ines/?$', views.addMines, name='addMines'),
    url(r'^submit[m,M]ines/?$', views.submitMines, name='submitMines'),
    url(r'^update[m,M]ines/(\d+)/?$', views.updateMines, name='updateMines'),
    url(r'^delete[m,M]ines/(\d+)/?$', views.deleteMines, name='deleteMines'),
    url(r'^view[m,M]ines/(\d+)/?$', views.viewMines, name='viewMines'),

    #Company pages
    url(r'^list[c,C]ompany/?$', views.listCompany, name='listCompany'),
    url(r'^add[c,C]ompany/?$', views.addCompany, name='addCompany'),
    url(r'^submit[c,C]ompany/?$', views.submitCompany, name='submitCompany'),
    url(r'^update[c,C]ompany/(\d+)/?$', views.updateCompany, name='updateCompany'),
    url(r'^delete[c,C]ompany/(\d+)/?$', views.deleteCompany, name='deleteCompany'),
    url(r'^view[c,C]ompany/(\d+)/?$', views.viewCompany, name='viewCompany'),

    #Mineral pages
    url(r'^list[m,M]ineral/?$', views.listMineral, name='listMineral'),
    url(r'^add[m,M]ineral/?$', views.addMineral, name='addMineral'),
    url(r'^submit[m,M]ineral/?$', views.submitMineral, name='submitMineral'),
    url(r'^update[m,M]ineral/(\d+)/?$', views.updateMineral, name='updateMineral'),
    url(r'^delete[m,M]ineral/(\d+)/?$', views.deleteMineral, name='deleteMineral'),
    url(r'^view[m,M]ineral/(\d+)/?$', views.viewMineral, name='viewMineral'),


]
