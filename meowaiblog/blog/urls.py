from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('demo', views.demo, name='demo'),
    path('', views.index, name='index')
]