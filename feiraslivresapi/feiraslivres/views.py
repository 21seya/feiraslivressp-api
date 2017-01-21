import django_filters

from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .filters import FeiraFilter
from .models import Feira
from .serializers import FeiraSerializer

'''
Para cada modelo, há 2 classes, que herdam de:
    . ListCreateAPIView: GET / POST em uma coleção de dados (list)
    . RetrieveUpdateDestroyAPIView: GET / PUT / PATCH / DELETE em um único objeto (detail)
No fim, há a classe ApiRoot, que é o endpoint de acesso para outros models.
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
