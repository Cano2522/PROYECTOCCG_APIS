from rest_framework import serializers
from datosgeograficos.models import (
    Pais,
    Estado,
    Mundeleg,
    CP,
)

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ['idPais', 'nombre', 'ISO', 'codNumIso', 'formDirec']

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ['idEstado', 'nombre', 'ISO', 'fk_Pais']

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mundeleg
        fields = ['idMunDeleg', 'nombre', 'fk_Estado']

class CPSerializer(serializers.ModelSerializer):
    class Meta:
        model = CP
        fields = ['cp', 'fk_MunDeleg']