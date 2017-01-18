from django.db import models

#class Feiras(models.Model):


# class FeirasLivresSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     LONG = serializers.CharField(requerid=True, allow_blank=True,
#                                  max_length=20)
#     LAT = serializers.CharField(requerid=True, allow_blank=True,
#                                 max_length=20)
#     SETCENS = serializers.IntegerField(requerid=True, allow_blank=True,
#                                        max_length=20)
#     AREAP = serializers.IntegerField(requerid=True, allow_blank=True,
#                                      max_length=20)
#     CODDIST = serializers.IntegerField(requerid=True, allow_blank=True,
#                                        max_length=5)
#     DISTRITO = serializers.CharField(requerid=True, allow_blank=True,
#                                      max_length=20)
#     CODSUBPREF = serializers.IntegerField(requerid=True, allow_blank=True,
#                                           max_length=5)
#     SUBPREFE = serializers.CharField(requerid=True, allow_blank=True,
#                                      max_length=50)
#     REGIAO5 = serializers.CharField(requerid=True, allow_blank=True,
#                                     max_length=20)
#     REGIAO8 = serializers.CharField(requerid=True, allow_blank=True,
#                                     max_length=20)
#     NOME_FEIRA = serializers.CharField(requerid=True, allow_blank=True,
#                                        max_length=50)
#     REGISTRO = serializers.CharField(requerid=True, allow_blank=True,
#                                      max_length=20)
#     LOGRADOURO = serializers.CharField(requerid=True, allow_blank=True,
#                                        max_length=50)
#     NUMERO = serializers.IntegerField(requerid=True, allow_blank=True,
#                                       max_length=6)
#     BAIRRO = serializers.CharField(requerid=True, allow_blank=True,
#                                    max_length=50)
#     REFERENCIA = serializers.CharField(requerid=True, allow_blank=True,
#                                        max_length=50)

    # def create(self, validated_data):
    #     """
    #     Create and return a new `FeiraLivre`, given the validated data.
    #     """
    #     return Snippet.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `FeiraLivre`, given the validated data.
    #     """
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.code = validated_data.get('code', instance.code)
    #     instance.linenos = validated_data.get('linenos', instance.linenos)
    #     instance.language = validated_data.get('language', instance.language)
    #     instance.style = validated_data.get('style', instance.style)
    #     instance.save()
    #     return instance