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
    url(r'^$', views.board_restful_main.as_view(), name='board_list'),
    url(r'^board_list/create$', views.board_restful_create.as_view(), name='board_create'),
    url(r'^board_list/(?P<id>\d+)/$', views.board_restful_detail.as_view(), name='board_detail'),
    url(r'^board_list/(?P<id>\d+)/update$', views.board_restful_update.as_view(), name='board_update'),
    url(r'^board_list/(?P<id>\d+)/updatePostHit$', views.board_restful_updatePostHit.as_view(), name='board_updatePostHit'),
    url(r'^board_list/(?P<id>\d+)/delete$', views.board_restful_delete.as_view(), name='board_delete'),
    url(r'^board_list/new$', views.board_restful_new.as_view(), name='board_new'),
    url(r'^board_list/hot$', views.board_restful_hot.as_view(), name='board_hot'),
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]