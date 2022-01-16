from django.urls import path
from . import views

urlpatterns = [
    path('', views.hook_list, name='hook_list'),
    path('hooks/<int:pk>', views.hook_info, name='hook_info'),

    path('hooks/new', views.hook_create, name='hook_create'),

]