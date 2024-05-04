from . import views
from django.urls import path

urlpatterns = [path('main/', views.index),
               path('v1/', views.main, name='aza1'),
               path('v2/', views.aza, name='aza2'),
               path('v3/', views.asa, name='aza3')
               ]
