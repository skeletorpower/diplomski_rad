from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('animations', views.AnimationView)
router.register('keyframes', views.KeyFrameView)


urlpatterns = [
    path('', include(router.urls))
]
