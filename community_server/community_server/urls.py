from django.conf.urls import url, include
from django.urls import path
# from rest_framework import routers
from django.contrib import admin
from board import views
from django.conf import settings
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
app_name = 'board_restful_main'
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^imageapi/',include('image.urls')),
    url(r'^board/',include('board.urls')),
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)