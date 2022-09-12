from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from usuarios.authentication_mixins import Authentication
from omniclass23.serializers import (
    OMC23Nivel1Serializer,
    OMC23Nivel2Serializer,
    OMC23Nivel3Serializer,
    OMC23Nivel4Serializer,
    OMC23Nivel5Serializer,
    OMC23Nivel6Serializer,
)

# Create your views here.
class OMC23Nivel1(Authentication,viewsets.ModelViewSet):
    serializer_class = OMC23Nivel1Serializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idOmc23N1 = pk).first()
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensaje':'Registro creado','data':serializer.data},status = status.HTTP_201_CREATED)
        return Response({'error':serializer.errors},status = status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'mensaje':'Registro actualizado','data':serializer.data}, status=status.HTTP_200_OK)
            return Response({'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe un registro con estos datos!'}, status = status.HTTP_404_NOT_FOUND)

    def destroy(self,request,pk=None):
        registro = self.get_queryset().filter(idOmc23N1=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un registro con estos datos!'}, status = status.HTTP_404_NOT_FOUND)

class OMC23Nivel2(Authentication,viewsets.ModelViewSet):
    serializer_class = OMC23Nivel2Serializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idOmc23N2 = pk).first()
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensaje':'Registro creado','data':serializer.data},status = status.HTTP_201_CREATED)
        return Response({'error':serializer.errors},status = status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'mensaje':'Registro actualizado','data':serializer.data}, status=status.HTTP_200_OK)
            return Response({'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe un registro con estos datos!'}, status = status.HTTP_404_NOT_FOUND)

    def destroy(self,request,pk=None):
        registro = self.get_queryset().filter(idOmc23N2=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un registro con estos datos!'}, status = status.HTTP_404_NOT_FOUND)

class OMC23Nivel3(Authentication,viewsets.ModelViewSet):
    serializer_class = OMC23Nivel3Serializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idOmc23N3 = pk).first()
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensaje':'Registro creado','data':serializer.data},status = status.HTTP_201_CREATED)
        return Response({'error':serializer.errors},status = status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'mensaje':'Registro actualizado','data':serializer.data}, status=status.HTTP_200_OK)
            return Response({'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe un registro con estos datos!'}, status = status.HTTP_404_NOT_FOUND)

    def destroy(self,request,pk=None):
        registro = self.get_queryset().filter(idOmc23N3=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un registro con estos datos!'}, status = status.HTTP_404_NOT_FOUND)

class OMC23Nivel4(Authentication,viewsets.ModelViewSet):
    serializer_class = OMC23Nivel4Serializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idOmc23N4 = pk).first()
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensaje':'Registro creado','data':serializer.data},status = status.HTTP_201_CREATED)
        return Response({'error':serializer.errors},status = status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'mensaje':'Registro actualizado','data':serializer.data}, status=status.HTTP_200_OK)
            return Response({'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe un registro con estos datos!'}, status = status.HTTP_404_NOT_FOUND)

    def destroy(self,request,pk=None):
        registro = self.get_queryset().filter(idOmc23N4=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un registro con estos datos!'}, status = status.HTTP_404_NOT_FOUND)

class OMC23Nivel5(Authentication,viewsets.ModelViewSet):
    serializer_class = OMC23Nivel5Serializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idOmc23N5 = pk).first()
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensaje':'Registro creado','data':serializer.data},status = status.HTTP_201_CREATED)
        return Response({'error':serializer.errors},status = status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'mensaje':'Registro actualizado','data':serializer.data}, status=status.HTTP_200_OK)
            return Response({'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe un registro con estos datos!'}, status = status.HTTP_404_NOT_FOUND)

    def destroy(self,request,pk=None):
        registro = self.get_queryset().filter(idOmc23N5=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un registro con estos datos!'}, status = status.HTTP_404_NOT_FOUND)

class OMC23Nivel6(Authentication,viewsets.ModelViewSet):
    serializer_class = OMC23Nivel6Serializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idOmc23N6 = pk).first()
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensaje':'Registro creado','data':serializer.data},status = status.HTTP_201_CREATED)
        return Response({'error':serializer.errors},status = status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'mensaje':'Registro actualizado','data':serializer.data}, status=status.HTTP_200_OK)
            return Response({'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe un registro con estos datos!'}, status = status.HTTP_404_NOT_FOUND)

    def destroy(self,request,pk=None):
        registro = self.get_queryset().filter(idOmc23N6=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un registro con estos datos!'}, status = status.HTTP_404_NOT_FOUND)
