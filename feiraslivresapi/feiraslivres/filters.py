import django_filters
from .models import Feira
from rest_framework import filters


class FeiraFilter(filters.FilterSet):
    distrito = django_filters.CharFilter(name='distrito',
                                         lookup_expr='icontains')
    regiao5 = django_filters.CharFilter(name="regiao5",
                                        lookup_expr='icontains')
    nome_feira = django_filters.CharFilter(name='nome_feira',
                                           lookup_expr='iexact')
    bairro = django_filters.CharFilter(name='bairro', lookup_expr='iexact')

    class Meta:
        model = Feira
        fields = ['distrito', 'regiao5', 'nome_feira', 'bairro']
