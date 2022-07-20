from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from unidadesmedida.serializers import (
    TipoUniMedSerializer,
    SubTipUniSerializer,
    UnidadesMedidaSerializer,
)
# Create your views here.

class VistaTipoUniMed(viewsets.ModelViewSet):
    serializer_class = TipoUniMedSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idTum = pk).first()

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response({'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe un Tipo de Unidad de Medida con esos datos'}, status = status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk=None):
        registro = self.get_queryset().filter(idTum=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Tipo de Unidad de Medida eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un Tipo de Unidad de Medida con estos datos!'}, status = status.HTTP_404_NOT_FOUND)

class VistaSubTipUni(viewsets.ModelViewSet):
    serializer_class = SubTipUniSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idStu = pk).first()

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response({'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe un Subtipo de Unidad de Medida con esos datos'}, status = status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk=None):
        registro = self.get_queryset().filter(idStu=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Subtipo de Unidad de Medida eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un Subtipo de Unidad de Medida con estos datos!'}, status = status.HTTP_404_NOT_FOUND)

class VistaUnidadesMedida(viewsets.ModelViewSet):
    serializer_class = UnidadesMedidaSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idUniMed = pk).first()

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response({'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe una Unidad de Medida con esos datos'}, status = status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk=None):
        registro = self.get_queryset().filter(idUniMed=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Unidad de Medida eliminada correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe una Unidad de Medida con estos datos!'}, status = status.HTTP_404_NOT_FOUND)