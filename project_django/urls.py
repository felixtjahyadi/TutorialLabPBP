"""project_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from wishlist.views import xml
from wishlist.views import show_json
from wishlist.views import json_id
from wishlist.views import show_wishlist_ajax
from wishlist.views import wishlist_form

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wishlist/', include('wishlist.urls')),
    path('xml/', xml, name='xml'),
    path('json/', show_json, name='json'),
    path('json/<int:id>', json_id, name='json_id'),
    path('ajax', show_wishlist_ajax, name='ajax'),
    path('ajax/submit', wishlist_form, name="form")
]
