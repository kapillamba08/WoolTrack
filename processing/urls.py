from django.urls import path
from . import views


urlpatterns = [
    path('', views.stage_list, name='stage_list'),
    path('new/', views.stage_create, name='stage_create'),
]

