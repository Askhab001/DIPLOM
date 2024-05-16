from . import views
from django.urls import path
from .views import create_post, post_list

urlpatterns = [
               path('', views.ford),
               path('v1/', views.main, name='aza1'),
               path('v2/', views.aza, name='aza2'),
               path('v3/', views.asa, name='aza3'),
               path('main/', create_post, name='command'),
               path('posts/', post_list, name='command1'),
               ]
