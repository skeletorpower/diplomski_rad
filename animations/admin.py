from django.contrib import admin
from .models import Animation, KeyFrame
# Register your models here.

class KeyFrameInline(admin.TabularInline):
    model = KeyFrame

class AnimationAdmin(admin.ModelAdmin):
    inlines = [
        KeyFrameInline
    ]

admin.site.register(Animation, AnimationAdmin)