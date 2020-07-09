"""assignmentProj1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.adminone,name="adminone"),
    path('loginpage/',views.loginpage,name="loginpage"),
    path('afterlogin/',views.afterlogin,name="afterlogin"),

    path('stockerone/',views.stockerone,name="stockerone"),
    path('savestocker/',views.savestocker,name="savestocker"),

    path('add_dispatcher/',views.add_dispatcher,name="add_dispatcher"),
    path('save_add_dispatcher/',views.save_add_dispatcher,name="save_add_dispatcher"),



    path('deletestocker/',views.deletestocker,name="deletestocker"),
    path('delete_add_dispatch/',views.delete_add_dispatch,name="delete_add_dispatch"),


]
