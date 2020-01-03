from django.shortcuts import render
from rest_framework import viewsets
from .models import Animation, KeyFrame
from .serializers import AnimationSerializer, KeyFrameSerializer
from django.core.serializers import serialize
from django.http import HttpResponse
from django.db.models import F
from rest_framework.decorators import action


# Create your views here.
def index(request):
    return HttpResponse("Hello world!")

def increment_like(request):
    return 1
class AnimationView(viewsets.ModelViewSet):
    queryset = Animation.objects.all()
    serializer_class = AnimationSerializer

    @action(methods=['post'], detail=True)
    def incrementLike(self, req, pk = None):
        animation, created = Animation.objects.get_or_create(id = pk)
        animation.likes += 1
        animation.save()
        return HttpResponse(animation)

    @action(methods=['post'], detail=True)
    def incrementDislike(self, req, pk = None):
        animation, created = Animation.objects.get_or_create(id = pk)
        animation.dislikes += 1
        animation.save()
        return HttpResponse(animation)
    

class KeyFrameView(viewsets.ModelViewSet):
    queryset = KeyFrame.objects.all()
    serializer_class = KeyFrameSerializer
