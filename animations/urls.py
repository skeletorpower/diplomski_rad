from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('animations', views.AnimationView)
router.register('animations/{animationId}/like', views.incrementLike, base_name='Like')
router.register('animations/{animationId}/dislike', views.incrementDislike, base_name='Dislike')
# router.register('keyframes', views.KeyFrameView)


urlpatterns = [
    path('', include(router.urls))
]
