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
        fields = ['idProveedor','Nombre','RFC','Email','Observaciones','logoImg','urlSitioWeb','Fabricante','Activo']

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['idMarca','Nombre','Activo']

class SectorMercadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectorMercado
        fields = ['idSecMer','Nombre']

class ProveedorMarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProveedorMarca
        fields = ['idProvMar','fk_Proveedor','fk_Marca']

class SucursalProvSerializer(serializers.ModelSerializer):
    class Meta:
        model = SucursalProv
        fields = ['idSucProv','Alias','numTel','contactoAten','nomSuperior','cargoSuperior','Calle','noInt','noExt','Colonia','fk_CP','fk_Proveedor']

class SectorProvSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectorProv
        fields = ['idSecProv','fk_Proveedor','fk_SecMer']
