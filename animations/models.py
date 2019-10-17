from django.db import models

# Create your models here.
class Animation(models.Model):
    name = models.CharField(max_length=50)
    time = models.IntegerField()

    def __str__(self):
        return self.name

class KeyFrame(models.Model):
    INTERPOLATIONS = (
        ('linear', 'Linear'),
        ('easy_in', 'Easy In'),
        ('easy_out', 'Easy Out'),
        ('easy_ease', 'Easy Ease')
    )
    key_frame = models.IntegerField()
    value = models.FloatField()
    interpolator = models.CharField(max_length=9, choices=INTERPOLATIONS, default='linear')
    animation = models.ForeignKey(Animation, related_name='keyframes', on_delete=models.CASCADE)

    def __str__(self):
        return "It's a key frame on "+str(self.key_frame)+" position with value of "+str(self.value)

    
    
