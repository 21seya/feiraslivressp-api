from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Feira
from .serializers import FeiraSerializer


@api_view(['GET', 'POST'])
def feira_list(request):
    if request.method == 'GET':
        feiras = Feira.objects.all()
        feiras_serializer = FeiraSerializer(feiras, many=True)
        return Response(feiras_serializer.data)
    elif request.method == 'POST':
        feira_serializer = FeiraSerializer(data=request.data)
        if feira_serializer.is_valid():
            feira_serializer.save()
            return Response(feira_serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(feira_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'POST', 'DELETE'])
def feira_detail(request, pk):
    try:
        feira = Feira.objects.get(pk=pk)
    except Feira.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        feira_serializer = FeiraSerializer(feira)
        return Response(feira_serializer.data)
    elif request.method == 'PUT':
        feira_serializer = FeiraSerializer(feira, data=request.data)
        if feira_serializer.is_valid():
            feira_serializer.save()
            return Response(feira_serializer.data)
        return Response(feira_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        feira.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

