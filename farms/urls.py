from django.urls import path
from . import views


urlpatterns = [
    path('', views.farm_list, name='farm_list'),
    path('new/', views.farm_create, name='farm_create'),
]

