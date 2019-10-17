from rest_framework import serializers
from .models import Animation, KeyFrame

class KeyFrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyFrame
        fields = ['id','key_frame','value','interpolator']

class AnimationSerializer(serializers.ModelSerializer):
    keyframes = KeyFrameSerializer(many=True)
    class Meta:
        model = Animation
        fields = ['id','name','time',"keyframes"]
