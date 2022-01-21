from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('hooks/', views.HookList.as_view(), name='hook_list'),
    path('hooks/<int:pk>', views.HookInfo.as_view(), name='hook_info'),

    path('yarns/', views.YarnList.as_view(), name='yarn_list'),
    path('yarns/<int:pk>', views.YarnInfo.as_view(), name='yarn_info'),

    path('stitches/', views.StitchList.as_view(), name='stitch_list'),
    path('stitches/<int:pk>', views.StitchInfo.as_view(), name='stitch_info'),

    path('gauges/', views.GaugeList.as_view(), name='gauge_list'),
    path('gauges/<int:pk>', views.GaugeInfo.as_view(), name='gauge_info'),

    path('patterns/', views.PatternList.as_view(), name='pattern_list'),
    path('patterns/<int:pk>', views.PatternInfo.as_view(), name='pattern_info'),


#---------------------------------------------------------------------------------

    # path('', views.hook_list, name='hook_list'),
    # path('hooks/<int:pk>', views.hook_info, name='hook_info'),

    # path('hooks/new', views.hook_create, name='hook_create'),
    # path('hooks/<int:pk>/edit', views.hook_update, name='hook_update'),
    # path('hooks/<int:pk>/delete', views.hook_delete, name='hook_delete'),

#---------------------------------------------------------------------------------

    # path('stitches/', views.stitch_list, name='stitch_list'),
    # path('stitches/<int:pk>', views.stitch_info, name='stitch_info'),

    # path('stitches/new', views.stitch_create, name='stitch_create'),
    # path('stitches/<int:pk>/edit', views.stitch_update, name='stitch_update'),
    # path('stitches/<int:pk>/delete', views.stitch_delete, name='stitch_delete'),

#---------------------------------------------------------------------------------

    # path('yarns/', views.yarn_list, name='yarn_list'),
    # path('yarns/<int:pk>', views.yarn_info, name='yarn_info'),

    # path('yarns/new', views.yarn_create, name='yarn_create'),
    # path('yarns/<int:pk>/edit', views.yarn_update, name='yarn_update'),
    # path('yarns/<int:pk>/delete', views.yarn_delete, name='yarn_delete'),

#---------------------------------------------------------------------------------

    # path('gauges/', views.gauge_list, name='gauge_list'),
    # path('gauges/<int:pk>', views.gauge_info, name='gauge_info'),

    # path('gauges/new', views.gauge_create, name='gauge_create'),
    # path('gauges/<int:pk>/edit', views.gauge_update, name='gauge_update'),
    # path('gauges/<int:pk>/delete', views.gauge_delete, name='gauge_delete'),

#---------------------------------------------------------------------------------

    # path('patterns/', views.pattern_list, name='pattern_list'),
    # path('patterns/<int:pk>', views.pattern_info, name='pattern_info'),

    # path('patterns/new', views.pattern_create, name='pattern_create'),
    # path('patterns/<int:pk>/edit', views.pattern_update, name='pattern_update'),
    # path('patterns/<int:pk>/delete', views.pattern_delete, name='pattern_delete'),
]