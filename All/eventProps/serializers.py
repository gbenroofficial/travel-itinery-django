from rest_framework import serializers
from eventProps.models import EventProp

#initializing the serializer field using the model:
class EventSerializer(serializers.ModelSerializer):    
    class Meta:
        model = EventProp
        fields = "__all__"
