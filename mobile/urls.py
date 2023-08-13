"""
URL configuration for DPS project.

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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page, name="home"),
    path('mobile/add/', views.add_mobile, name="add_mobile"),
    path('brand/add/', views.add_brand, name="add_brand"),
    path('mobile/<int:id>', views.edit_mobile, name="edit_mobile"),
    path('brand/<int:id>', views.edit_brand, name="edit_brand"),
    path('mobiles/', views.show_mobiles, name="show_mobiles"),
    path('brands/', views.show_brands, name="show_brands"),
    path('reports/', views.reports_page, name="reports"),
    path('forms/', views.forms_page, name="forms"),
]
