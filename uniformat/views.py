from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from usuarios.authentication_mixins import Authentication
from uniformat.serializers import (
    UFTCategoriaSerializer,
    UFTNivel2Serializer,
    UFTNivel3Serializer,
    UFTNivel4Serializer,
    UFTNivel5Serializer,
)
# Create your views here.

class UFTNivel1(Authentication,viewsets.ModelViewSet):
    serializer_class = UFTCategoriaSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idUftCat = pk).first()

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensaje':'Registro creado','data':serializer.data},status = status.HTTP_201_CREATED)
        return Response({'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'mensaje':'Registro actualizado','data':serializer.data}, status=status.HTTP_200_OK)
            return Response({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe un registro esos datos'}, status = status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk=None):
        registro = self.get_queryset().filter(idUftCat=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un registro con estos datos!'}, status = status.HTTP_404_NOT_FOUND)

class UFTNivel2(Authentication,viewsets.ModelViewSet):
    serializer_class = UFTNivel2Serializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idUftN2 = pk).first()

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensaje':'Registro creado','data':serializer.data},status = status.HTTP_201_CREATED)
        return Response({'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'mensaje':'Registro actualizado','data':serializer.data}, status=status.HTTP_200_OK)
            return Response({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe un registro esos datos'}, status = status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk=None):
        registro = self.get_queryset().filter(idUftN2=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un registro con estos datos!'}, status = status.HTTP_404_NOT_FOUND)

class UFTNivel3(Authentication,viewsets.ModelViewSet):
    serializer_class = UFTNivel3Serializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idUftN3 = pk).first()

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensaje':'Registro creado','data':serializer.data},status = status.HTTP_201_CREATED)
        return Response({'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'mensaje':'Registro actualizado','data':serializer.data}, status=status.HTTP_200_OK)
            return Response({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe un registro esos datos'}, status = status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk=None):
        registro = self.get_queryset().filter(idUftN3=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un registro con estos datos!'}, status = status.HTTP_404_NOT_FOUND)

class UFTNivel4(Authentication,viewsets.ModelViewSet):
    serializer_class = UFTNivel4Serializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idUftN4 = pk).first()

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensaje':'Registro creado','data':serializer.data},status = status.HTTP_201_CREATED)
        return Response({'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'mensaje':'Registro actualizado','data':serializer.data}, status=status.HTTP_200_OK)
            return Response({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe un registro esos datos'}, status = status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk=None):
        registro = self.get_queryset().filter(idUftN4=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un registro con estos datos!'}, status = status.HTTP_404_NOT_FOUND)

class UFTNivel5(Authentication,viewsets.ModelViewSet):
    serializer_class = UFTNivel5Serializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idUftN5 = pk).first()

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensaje':'Registro creado','data':serializer.data},status = status.HTTP_201_CREATED)
        return Response({'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'mensaje':'Registro actualizado','data':serializer.data}, status=status.HTTP_200_OK)
            return Response({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe un registro esos datos'}, status = status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk=None):
        registro = self.get_queryset().filter(idUftN5=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un registro con estos datos!'}, status = status.HTTP_404_NOT_FOUND)