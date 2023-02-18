from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from .models import ThresholdValue 
from .serializers import RangeSerializer


# Create your views here.

@api_view(['GET'])
def getrange(request):
    value=ThresholdValue.objects.all()
    serializer=RangeSerializer(value,many=True)
    return Response(serializer.data) 
 


@api_view(['POST'])
def setrange(request):
    task = ThresholdValue.objects.get(id = 1)
    serializer = RangeSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)