from django.db import models
from django.utils import timezone
from phone_field import PhoneField

class EventProp(models.Model):
    name = models.TextField(default="")
    description = models.TextField(default="")
    
    """ location = models.CharField(max_length=255)
     """
    # price = models.CharField(max_length=255, null=True)
    """ time = models.TimeField()
    rate = models.PositiveSmallIntegerField()
    likes= models.PositiveIntegerField(default=0)
    image = models.CharField(max_length=255)
    dislikes = models.PositiveIntegerField(default=0)
    website = models.CharField(max_length=255) """

    def __str__(self):
        return self.name