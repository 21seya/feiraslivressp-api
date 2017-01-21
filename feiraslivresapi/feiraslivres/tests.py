"""
Os testes aqui foram inspirados pelo seguinte projeto:
https://github.com/erkarl/django-rest-framework-oauth2-provider-example/blob/master/apps/users/tests.py
"""

from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase

from .models import Feira
from .serializers import FeiraSerializer

FIXTURES = {
    "feira1": {
        "id": 1,
        "longi": "-99990001",
        "lat": "-99990001",
        "setcens": "999999999000001",
        "areap": "9999999000001",
        "coddist": 1,
        "distrito": "BAIRRO B",
        "codsubpref": 1,
        "subprefe": "GENERICA-SP",
        "regiao5": "Centro",
        "regiao8": "Centro-1",
        "nome_feira": "GENERICA SP 1",
        "registro": "9999-1",
        "logradouro": "RUA X",
        "numero": "001A",
        "bairro": "CENTRO",
        "referencia": "CENTRO DE SP"
    },
    "feira2": {
        "id": 2,
        "longi": "-99990002",
        "lat": "-99990002",
        "setcens": "999999999000002",
        "areap": "9999999000002",
        "coddist": 2,
        "distrito": "BAIRRO B",
        "codsubpref": 2,
        "subprefe": "GENERICA-SP-2",
        "regiao5": "Centro",
        "regiao8": "Centro-2",
        "nome_feira": "GENERICA SP 2",
        "registro": "9999-2",
        "logradouro": "RUA X",
        "numero": "002A",
        "bairro": "CENTRO",
        "referencia": "CENTRO DE SP"
    }
}


class CreateFeiraTest(APITestCase):
    def setUp(self):
        self.feira1 = FIXTURES['feira1']
        self.feira2 = FIXTURES['feira2']

    def test_can_create_feiras(self):
        response1 = self.client.post(reverse('feira-list'), self.feira1)
        response2 = self.client.post(reverse('feira-list'), self.feira2)

        feira1 = Feira.objects.get(pk=FIXTURES['feira1']['id'])
        feira2 = Feira.objects.get(pk=FIXTURES['feira2']['id'])

        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED)

        self.assertEqual(feira1.nome_feira, 'GENERICA SP 1')
        self.assertEqual(feira2.nome_feira, 'GENERICA SP 2')


class ReadFeiraTest(APITestCase):
    def setUp(self):
        self.feira1 = Feira.objects.create(
            id=FIXTURES['feira1']['id'],
            longi=FIXTURES['feira1']['longi'],
            lat=FIXTURES['feira1']['lat'],
            setcens=FIXTURES['feira1']['setcens'],
            areap=FIXTURES['feira1']['areap'],
            coddist=FIXTURES['feira1']['coddist'],
            distrito=FIXTURES['feira1']['distrito'],
            codsubpref=FIXTURES['feira1']['codsubpref'],
            subprefe=FIXTURES['feira1']['subprefe'],
            regiao5=FIXTURES['feira1']['regiao5'],
            regiao8=FIXTURES['feira1']['regiao8'],
            nome_feira=FIXTURES['feira1']['nome_feira'],
            registro=FIXTURES['feira1']['registro'],
            logradouro=FIXTURES['feira1']['logradouro'],
            numero=FIXTURES['feira1']['numero'],
            bairro=FIXTURES['feira1']['bairro'],
            referencia=FIXTURES['feira1']['referencia']
        )

        self.feira2 = Feira.objects.create(
            id=FIXTURES['feira2']['id'],
            longi=FIXTURES['feira2']['longi'],
            lat=FIXTURES['feira2']['lat'],
            setcens=FIXTURES['feira2']['setcens'],
            areap=FIXTURES['feira2']['areap'],
            coddist=FIXTURES['feira2']['coddist'],
            distrito=FIXTURES['feira2']['distrito'],
            codsubpref=FIXTURES['feira2']['codsubpref'],
            subprefe=FIXTURES['feira2']['subprefe'],
            regiao5=FIXTURES['feira2']['regiao5'],
            regiao8=FIXTURES['feira2']['regiao8'],
            nome_feira=FIXTURES['feira2']['nome_feira'],
            registro=FIXTURES['feira2']['registro'],
            logradouro=FIXTURES['feira2']['logradouro'],
            numero=FIXTURES['feira2']['numero'],
            bairro=FIXTURES['feira2']['bairro'],
            referencia=FIXTURES['feira2']['referencia']
        )

    def test_can_read_feira_list(self):
        response = self.client.get(reverse('feira-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_feira_detail(self):
        response = self.client.get(reverse('feira-detail', args=[self.feira1.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateFeiraTest(APITestCase):
    def setUp(self):
        self.feira1 = Feira.objects.create(
            id=FIXTURES['feira1']['id'],
            longi=FIXTURES['feira1']['longi'],
            lat=FIXTURES['feira1']['lat'],
            setcens=FIXTURES['feira1']['setcens'],
            areap=FIXTURES['feira1']['areap'],
            coddist=FIXTURES['feira1']['coddist'],
            distrito=FIXTURES['feira1']['distrito'],
            codsubpref=FIXTURES['feira1']['codsubpref'],
            subprefe=FIXTURES['feira1']['subprefe'],
            regiao5=FIXTURES['feira1']['regiao5'],
            regiao8=FIXTURES['feira1']['regiao8'],
            nome_feira=FIXTURES['feira1']['nome_feira'],
            registro=FIXTURES['feira1']['registro'],
            logradouro=FIXTURES['feira1']['logradouro'],
            numero=FIXTURES['feira1']['numero'],
            bairro=FIXTURES['feira1']['bairro'],
            referencia=FIXTURES['feira1']['referencia']
        )

        self.feira2 = Feira.objects.create(
            id=FIXTURES['feira2']['id'],
            longi=FIXTURES['feira2']['longi'],
            lat=FIXTURES['feira2']['lat'],
            setcens=FIXTURES['feira2']['setcens'],
            areap=FIXTURES['feira2']['areap'],
            coddist=FIXTURES['feira2']['coddist'],
            distrito=FIXTURES['feira2']['distrito'],
            codsubpref=FIXTURES['feira2']['codsubpref'],
            subprefe=FIXTURES['feira2']['subprefe'],
            regiao5=FIXTURES['feira2']['regiao5'],
            regiao8=FIXTURES['feira2']['regiao8'],
            nome_feira=FIXTURES['feira2']['nome_feira'],
            registro=FIXTURES['feira2']['registro'],
            logradouro=FIXTURES['feira2']['logradouro'],
            numero=FIXTURES['feira2']['numero'],
            bairro=FIXTURES['feira2']['bairro'],
            referencia=FIXTURES['feira2']['referencia']
        )

        '''
        Eu tive que adicionar o código abaixo setando o serializer em um
        contexto explícito porque caso contrário o serializador terá problemas
        quando houver listado a "url" em sua lista de campos Meta.
        O erro apontado antes de definir explicitamente o contexto do serializador,
        foi semelhante à este:

        AssertionError: `HyperlinkedIdentityField` requires the request in the serializer context.
        Add `context={'request': request}` when instantiating the serializer

        Este thread stackoverflow ajudou a resolvê-lo:
        Http://stackoverflow.com/questions/34438290/assertionerror-hyperlinkedidentityfield-requires-the-request-in-the-serialize
        '''
        factory = APIRequestFactory()
        request = factory.get('/')
        serializer_context = {
            'request': Request(request)
        }

        # Serializer aqui produz um dict
        self.feira1_data = FeiraSerializer(self.feira1, context=serializer_context).data
        # Abaixo nós atualizamos este dict definindo os valores que queremos mudar (nome_feira)
        self.feira1_data.update({'nome_feira': 'GENERICA SP 1 *** CHANGED'})

        # Abaixo funciona exatamente como o caso de "self.feira1_data"
        self.feira2_data = FeiraSerializer(self.feira2, context=serializer_context).data
        self.feira2_data.update({'nome_feira': 'GENERICA SP 2 *** CHANGED'})

    def test_can_update_feiras(self):
        response1 = self.client.put(reverse('feira-detail', args=[self.feira1.id]), self.feira1_data)
        self.assertEqual(response1.status_code, status.HTTP_200_OK)

        response2 = self.client.put(reverse('feira-detail', args=[self.feira2.id]), self.feira2_data)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)


class DeleteUserTest(APITestCase):
    def setUp(self):
        self.feira1 = Feira.objects.create(
            id=FIXTURES['feira1']['id'],
            longi=FIXTURES['feira1']['longi'],
            lat=FIXTURES['feira1']['lat'],
            setcens=FIXTURES['feira1']['setcens'],
            areap=FIXTURES['feira1']['areap'],
            coddist=FIXTURES['feira1']['coddist'],
            distrito=FIXTURES['feira1']['distrito'],
            codsubpref=FIXTURES['feira1']['codsubpref'],
            subprefe=FIXTURES['feira1']['subprefe'],
            regiao5=FIXTURES['feira1']['regiao5'],
            regiao8=FIXTURES['feira1']['regiao8'],
            nome_feira=FIXTURES['feira1']['nome_feira'],
            registro=FIXTURES['feira1']['registro'],
            logradouro=FIXTURES['feira1']['logradouro'],
            numero=FIXTURES['feira1']['numero'],
            bairro=FIXTURES['feira1']['bairro'],
            referencia=FIXTURES['feira1']['referencia']
        )

        self.feira2 = Feira.objects.create(
            id=FIXTURES['feira2']['id'],
            longi=FIXTURES['feira2']['longi'],
            lat=FIXTURES['feira2']['lat'],
            setcens=FIXTURES['feira2']['setcens'],
            areap=FIXTURES['feira2']['areap'],
            coddist=FIXTURES['feira2']['coddist'],
            distrito=FIXTURES['feira2']['distrito'],
            codsubpref=FIXTURES['feira2']['codsubpref'],
            subprefe=FIXTURES['feira2']['subprefe'],
            regiao5=FIXTURES['feira2']['regiao5'],
            regiao8=FIXTURES['feira2']['regiao8'],
            nome_feira=FIXTURES['feira2']['nome_feira'],
            registro=FIXTURES['feira2']['registro'],
            logradouro=FIXTURES['feira2']['logradouro'],
            numero=FIXTURES['feira2']['numero'],
            bairro=FIXTURES['feira2']['bairro'],
            referencia=FIXTURES['feira2']['referencia']
        )

    def test_can_delete_feiras(self):
        response1 = self.client.delete(reverse('feira-detail', args=[self.feira1.id]))
        self.assertEqual(response1.status_code, status.HTTP_204_NO_CONTENT)

        response2 = self.client.delete(reverse('feira-detail', args=[self.feira2.id]))
        self.assertEqual(response2.status_code, status.HTTP_204_NO_CONTENT)

        # Como removemos ambos os registros, o banco de dados deve estar vazio também
        feiras = Feira.objects.all()
        self.assertEqual(feiras.count(), 0)


class ModelTest(APITestCase):
    def test_feira_representation(self):
        self.feira = Feira.objects.create(
            id=777,
            nome_feira='Feira do Zé',
            bairro='Centro'
        )
        self.assertEqual(str(self.feira), 'nome: Feira do Zé, bairro: Centro')
