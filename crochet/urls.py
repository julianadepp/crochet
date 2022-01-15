from django.urls import path
from . import views

urlpatterns = [
    path('', views.hook_list, name='hook_list'),
]