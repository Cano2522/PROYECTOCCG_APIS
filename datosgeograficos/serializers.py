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
        fields = ['idPais', 'Nombre', 'ISO', 'codNumIso', 'formDirec']

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ['idEstado', 'Nombre', 'ISO', 'fk_Pais']

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mundeleg
        fields = ['idMunDeleg', 'Nombre', 'fk_Estado']

class CPSerializer(serializers.ModelSerializer):
    class Meta:
        model = CP
        fields = ['cp', 'fk_MunDeleg']