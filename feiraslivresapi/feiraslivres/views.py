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
    filter_backends = (filters.DjangoFilterBackend,)
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
