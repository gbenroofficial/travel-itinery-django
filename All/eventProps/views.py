from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import EventSerializer
from .models import EventProp


# Create your views here.
def home(request):    

    return render(request, "index.html")

@api_view(['GET'])
def showIndex(request):
    if request.method == 'GET':
        events = EventProp.objects.all()
        serialized = EventSerializer(events, many=True)
        data = serialized.data
        data = {"data": data}
        #print(data)
        # return render(request, "index.html", data)
        return Response(data)

@api_view(['GET', 'POST'])
def eventAction(request):
    if request.method == 'GET':
        events = EventProp.objects.all()
        serialized = EventSerializer(events, many=True)
        return Response(serialized.data)

    elif request.method == 'POST':
        serialized = EventSerializer(data= request.data)
        if serialized.is_valid():
            p = serialized.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def eventDelete(request, pk):
    try:
        event = EventProp.objects.get(pk == pk)
    except EventProp.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
