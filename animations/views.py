from django.shortcuts import render
from rest_framework import viewsets
from .models import Animation, KeyFrame
from .serializers import AnimationSerializer, KeyFrameSerializer
from django.core.serializers import serialize
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello world!")

class AnimationView(viewsets.ModelViewSet):
    queryset = Animation.objects.all()
    serializer_class = AnimationSerializer

class KeyFrameView(viewsets.ModelViewSet):
    queryset = KeyFrame.objects.all()
    serializer_class = KeyFrameSerializer



