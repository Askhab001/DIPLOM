from . import views
from django.urls import path

urlpatterns = [path('', views.index),
               path('v1/', views.main, name='aza1'),
               path('v2/', views.aza, name='aza2'),
               path('v3/', views.asa, name='aza3'),
               path('create/', views.create_command, name='command'),
               path('main/', views.command_list, name='command_list'),
               ]
