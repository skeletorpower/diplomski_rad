from django.shortcuts import render
from rest_framework import viewsets
from .models import Animation, KeyFrame, Like, Dislike
from .serializers import AnimationSerializer, KeyFrameSerializer
from django.core.serializers import serialize
from django.http import HttpResponse
from django.db.models import F


# Create your views here.
def index(request):
    return HttpResponse("Hello world!")

class AnimationView(viewsets.ModelViewSet):
    queryset = Animation.objects.all()
    serializer_class = AnimationSerializer

    

class KeyFrameView(viewsets.ModelViewSet):
    queryset = KeyFrame.objects.all()
    serializer_class = KeyFrameSerializer


def incrementLike(self, request, animationId):
        animation = get_object_or_404(Animation, id=animationId)
        animation.like = F('like') + 1
        animation.save()
        return redirect('animations')
    
def incrementDislike(self, request, animationId):
    animation = get_object_or_404(Animation, id=animationId)
    animation.like = F('dislike') + 1
    animation.save()
    return redirect('animations')


