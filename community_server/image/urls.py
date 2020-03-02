from django.conf.urls import url,include 
from django.contrib import admin 
from rest_framework import routers
from django.urls import path 
from image.views import *
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings
router = routers.DefaultRouter()
router.register('image', image_view_set)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
]
