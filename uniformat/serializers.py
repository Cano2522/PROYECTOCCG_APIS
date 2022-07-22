from rest_framework import serializers
from uniformat.models import (
    UFTCategorias,
    UFTNivel2,
    UFTNivel3,
    UFTNivel4,
    UFTNivel5,
)

#nivel 1
class UFTCategoriaSerializer(serializers.ModelSerializer):
    """ Serializador para objetos de la tabla UFTCategorias """
    class Meta:
        model = UFTCategorias
        fields = ('idUftCat', 'codigo', 'descriEng', 'descriSpa')

#nivel 2
class UFTNivel2Serializer(serializers.ModelSerializer):
    """ Serializador para objetos de la tabla UFTCategorias """
    class Meta:
        model = UFTNivel2
        fields = ('idUftN2', 'codigo', 'descriEng', 'descriSpa', 'explicacionEng', 'explicacionSpa', 'fk_UftCat')

#nivel 3
class UFTNivel3Serializer(serializers.ModelSerializer):
    """ Serializador para objetos de la tabla UFTCategorias """
    class Meta:
        model = UFTNivel3
        fields = ('idUftN3', 'codigo', 'descriEng', 'descriSpa', 'explicacionEng', 'explicacionSpa', 'observaciones', 'fk_UftN2')

#Nivel 4
class UFTNivel4Serializer(serializers.ModelSerializer):
    """ Serializador para objetos de la tabla UFTCategorias """
    class Meta:
        model = UFTNivel4
        fields = ('idUftN4', 'codigo', 'descriEng', 'descriSpa', 'explicacionEng', 'explicacionSpa', 'observaciones', 'fk_UftN3')

#nivel 5
class UFTNivel5Serializer(serializers.ModelSerializer):
    """ Serializador para objetos de la tabla UFTCategorias """
    class Meta:
        model = UFTNivel5
        fields = ('idUftN5', 'codigo', 'descriEng', 'descriSpa', 'explicacionEng', 'explicacionSpa', 'observaciones', 'fk_UftN4')


