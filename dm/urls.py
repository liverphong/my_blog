from django.conf.urls import url
from django.urls import path, re_path
from . import views
urlpatterns = [
    path('dm/', views.dm, name='dm'),
    re_path('cj1/', views.cj1, name='cj1'),
    re_path('cj2/', views.cj2, name='cj2'),

]