from dataclasses import fields
from rest_framework import serializers
from proveedores.models import (
    Proveedor,
    Marca,
    SectorMercado,
    ProveedorMarca,
    SucursalProv,
    SectorProv,
)

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ['idProveedor','nombre','RFC','email','fabricante','activo','observaciones','logoImg','urlSitioWeb']

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['idMarca','nombre','activo']

class SectorMercadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectorMercado
        fields = ['idSecMer','nombre']

class ProveedorMarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProveedorMarca
        fields = ['idProvMar','fk_Proveedor','fk_Marca']

class SucursalProvSerializer(serializers.ModelSerializer):
    class Meta:
        model = SucursalProv
        fields = ['idSucProv','alias','numTel','contactoAten','nomSuperior','cargoSuperior','calle','noInt','noExt','colonia','fk_CP','fk_Proveedor']

class SectorProvSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectorProv
        fields = ['idSecProv','fk_Proveedor','fk_SecMer']
