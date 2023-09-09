from django.urls import path 
from . import views

# one urlpattern per line
urlpatterns = [
    path('', views.index, name='index'),
    path('status', views.status, name='status'),
    path('about', views.about, name='about'),
    path('drivers', views.drivers, name='drivers'),
]