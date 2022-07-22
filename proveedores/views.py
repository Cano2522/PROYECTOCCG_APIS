from django.db import connection
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from usuarios.authentication_mixins import Authentication
from proveedores.serializers import (
    ProveedorSerializer,
    MarcaSerializer,
    SectorMercadoSerializer,
    ProveedorMarcaSerializer,
    SucursalProvSerializer,
    SectorProvSerializer
)

# Create your views here.

#TABLAS PRINCIPALES O PURAS

class VistaProveedor(Authentication,viewsets.ModelViewSet):
    serializer_class = ProveedorSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idProveedor=pk).first()
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response({'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response({'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe un registro con esos datos.'}, status = status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk=None):
        proveedor = self.get_queryset().filter(idProveedor=pk).first()
        if proveedor:
            proveedor.delete()
            return Response({'mensaje':'Registro eliminado correctamente.'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un registro con estos datos.'}, status = status.HTTP_404_NOT_FOUND)

class VistaMarca(Authentication,viewsets.ModelViewSet):
    serializer_class = MarcaSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idMarca=pk).first()
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response({'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response({'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe un registro con esos datos.'}, status = status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk=None):
        marca = self.get_queryset().filter(idMarca=pk).first()
        if marca:
            marca.delete()
            return Response({'mensaje':'Registro eliminado correctamente.'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un registro con estos datos.'}, status = status.HTTP_404_NOT_FOUND)

class VistaSectorMercado(Authentication,viewsets.ModelViewSet):
    serializer_class = SectorMercadoSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idSecMer=pk).first()
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response({'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response({'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe un registro con esos datos.'}, status = status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk=None):
        registro = self.get_queryset().filter(idSecMer=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente.'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un registro con estos datos.'}, status = status.HTTP_404_NOT_FOUND)

class VistaProveedorMarca(Authentication,viewsets.ModelViewSet):
    serializer_class = ProveedorMarcaSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idProveedorMarca=pk).first()
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response({'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response({'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe un registro con esos datos.'}, status = status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk=None):
        registro = self.get_queryset().filter(idProveedorMarca=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente.'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un registro con estos datos.'},status = status.HTTP_404_NOT_FOUND)

class VistaSucursalProv(Authentication,viewsets.ModelViewSet):
    serializer_class = SucursalProvSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idSucProv=pk).first()
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response({'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response({'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe un registro con esos datos.'}, status = status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk=None):
        registro = self.get_queryset().filter(idSucProv=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente.'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un registro con estos datos.'},status = status.HTTP_404_NOT_FOUND)

class VistaSectorProv(Authentication,viewsets.ModelViewSet):
    serializer_class = SectorProvSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idSectorProv=pk).first()
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response({'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response({'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe un registro con esos datos.'}, status = status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk=None):
        registro = self.get_queryset().filter(idSectorProv=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente.'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un registro con estos datos.'},status = status.HTTP_404_NOT_FOUND)

class ListarSectorXProveedor(Authentication,viewsets.GenericViewSet):
    def get_queryset(self):
        with connection.cursor() as cursor:
            listarSector = cursor.execute("SELECT Proveedor.nombre AS NombreProv, Proveedor.RFC,Proveedor.email,Proveedor.observaciones,Proveedor.urlSitioWeb,Proveedor.fabricante,Proveedor.activo,SectorMercado.nombre AS NombreSector FROM Proveedor JOIN SectorProv ON fk_Proveedor=idProveedor JOIN SectorMercado ON fk_SecMer=idSecMer")
            listarSector = dictfetchall(cursor)
            return listarSector
        
    def list(self, request):
        data = self.get_queryset()
        if data:
            return Response(data, status = status.HTTP_200_OK)
        else:
            return Response({'mensaje':'No existen registros'}, status = status.HTTP_404_NOT_FOUND)

class ListarMarcaXProveedor(Authentication,viewsets.GenericViewSet):
    def get_queryset(self):
        with connection.cursor() as cursor:
            listarMarca = cursor.execute("SELECT Proveedor.nombre AS NombreProv,Proveedor.RFC,Proveedor.email,Proveedor.observaciones,Proveedor.urlSitioWeb,Proveedor.fabricante,Proveedor.activo,Marca.nombre AS NombreMarca,Marca.activo FROM Proveedor JOIN ProveedorMarca ON fk_Proveedor=idProveedor JOIN Marca ON fk_Marca=idMarca")
            listarMarca = dictfetchall(cursor)
            return listarMarca
        
    def list(self, request):
        data = self.get_queryset()
        if data:
            return Response(data, status = status.HTTP_200_OK)
        else:
            return Response({'mensaje':'No existen registros'}, status = status.HTTP_404_NOT_FOUND)

class ListarSucursalXProveedor(Authentication,viewsets.GenericViewSet):
    def get_queryset(self):
        with connection.cursor() as cursor:
            listarSucursal = cursor.execute("SELECT Proveedor.nombre,Proveedor.RFC,Proveedor.email,Proveedor.observaciones,Proveedor.urlSitioWeb,Proveedor.fabricante,Proveedor.activo,SucursalProv.alias,SucursalProv.numTel,SucursalProv.contactoAten,SucursalProv.nomSuperior, SucursalProv.cargoSuperior,SucursalProv.calle,SucursalProv.noInt,SucursalProv.noExt,SucursalProv.colonia,CP.cp AS CP,MunDeleg.nombre AS Municipio,Estado.nombre AS Estado,Pais.nombre AS Pais FROM Proveedor JOIN SucursalProv ON fk_Proveedor=idProveedor JOIN CP ON fk_CP=cp JOIN MunDeleg ON fk_MunDeleg=idMunDeleg JOIN Estado ON fk_Estado=idEstado JOIN Pais ON fk_Pais=idPais")
            listarSucursal = dictfetchall(cursor)
            return listarSucursal
        
    def list(self, request):
        data = self.get_queryset()
        if data:
            return Response(data, status = status.HTTP_200_OK)
        else:
            return Response({'mensaje':'No existen registros'}, status = status.HTTP_404_NOT_FOUND)

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
