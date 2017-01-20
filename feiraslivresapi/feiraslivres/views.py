import django_filters

from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .filters import FeiraFilter
from .models import Feira
from .serializers import FeiraSerializer

'''
For each model, there are 2 classes, that inherit from:
    . ListCreateAPIView: GET / POST on a collection (list)
    . RetrieveUpdateDestroyAPIView: GET / PUT / PATCH / DELETE on a single object (detail)
In the end, there is the ApiRoot class, that is the entry endpoint for all the other models.
'''


class FeiraList(generics.ListCreateAPIView):
    queryset = Feira.objects.all()
    serializer_class = FeiraSerializer
    filter_backends = (filters.DjangoFilterBackend)
    filter_class = FeiraFilter
    name = 'feira-list'


class FeiraDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feira.objects.all()
    serializer_class = FeiraSerializer
    name = 'feira-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'feiras': reverse(FeiraList.name, request=request)
        })

# @api_view(['GET', 'POST'])
# def feira_list(request):
#     if request.method == 'GET':
#         feiras = Feira.objects.all()
#         feiras_serializer = FeiraSerializer(feiras, many=True)
#         return Response(feiras_serializer.data)
#     elif request.method == 'POST':
#         feira_serializer = FeiraSerializer(data=request.data)
#         if feira_serializer.is_valid():
#             feira_serializer.save()
#             return Response(feira_serializer.data,
#                             status=status.HTTP_201_CREATED)
#         return Response(feira_serializer.errors,
#                         status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'POST', 'DELETE'])
# def feira_detail(request, pk):
#     try:
#         feira = Feira.objects.get(pk=pk)
#     except Feira.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         feira_serializer = FeiraSerializer(feira)
#         return Response(feira_serializer.data)
#     elif request.method == 'PUT':
#         feira_serializer = FeiraSerializer(feira, data=request.data)
#         if feira_serializer.is_valid():
#             feira_serializer.save()
#             return Response(feira_serializer.data)
#         return Response(feira_serializer.errors,
#                         status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         feira.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class FeiraViewSet(viewsets.ModelViewSet):
#     queryset = Feira.objects.all()
#     serializer_class = FeiraSerializer
#     filter_backends = (filters.DjangoFilterBackend)
#     filter_class = FeiraFilter
