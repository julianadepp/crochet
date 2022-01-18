from django.urls import path
from . import views

urlpatterns = [
    path('', views.hook_list, name='hook_list'),
    path('hooks/<int:pk>', views.hook_info, name='hook_info'),

    path('hooks/new', views.hook_create, name='hook_create'),
    path('hooks/<int:pk>/edit', views.hook_update, name='hook_update'),
    path('hooks/<int:pk>/delete', views.hook_delete, name='hook_delete'),


    path('stitches/', views.stitch_list, name='stitch_list'),
    path('stitches/<int:pk>', views.stitch_info, name='stitch_info'),

    path('stitches/new', views.stitch_create, name='stitch_create'),
    path('stitches/<int:pk>/edit', views.stitch_update, name='stitch_update'),
    path('stitches/<int:pk>/delete', views.stitch_delete, name='stitch_delete'),


    path('yarns/', views.yarn_list, name='yarn_list'),
    path('yarns/<int:pk>', views.yarn_info, name='yarn_info'),

    path('yarns/new', views.yarn_create, name='yarn_create'),
    path('yarns/<int:pk>/edit', views.yarn_update, name='yarn_update'),
    path('yarns/<int:pk>/delete', views.yarn_delete, name='yarn_delete'),
]