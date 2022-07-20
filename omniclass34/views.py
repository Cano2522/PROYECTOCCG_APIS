from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from omniclass34.serializers import (
    OMC34Nivel1Serializer,
    OMC34Nivel2Serializer,
    OMC34Nivel3Serializer,
    OMC34Nivel4Serializer,
)

# Create your views here.
class OMC34Nivel1(viewsets.ModelViewSet):
    serializer_class = OMC34Nivel1Serializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idOmc34N1 = pk).first()

    # def list(self, request):
    #     serializer = self.get_serializer(self.get_queryset(), many=True)
    #     return Response(serializer.data, status = status.HTTP_200_OK)
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response({'error':serializer.errors},status = status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe un Registro con estos datos!'}, status = status.HTTP_404_NOT_FOUND)

    def destroy(self,request,pk=None):
        registro = self.get_queryset().filter(idOmc34N1=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un Registro con estos datos!'}, status = status.HTTP_404_NOT_FOUND)

# TABLA OMNICLAS 34 Nivel 2
class OMC34Nivel2(viewsets.ModelViewSet):
    serializer_class = OMC34Nivel2Serializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idOmc34N2 = pk).first()

    # def list(self, request):
    #     serializer = self.get_serializer(self.get_queryset(), many=True)
    #     return Response(serializer.data, status = status.HTTP_200_OK)
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response({'error':serializer.errors},status = status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe un Registro con estos datos!'}, status = status.HTTP_404_NOT_FOUND)

    def destroy(self,request,pk=None):
        registro = self.get_queryset().filter(idOmc34N2=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un Registro con estos datos!'}, status = status.HTTP_404_NOT_FOUND)

# TABLA OMNICLAS 34 Nivel 3
class OMC34Nivel3(viewsets.ModelViewSet):
    serializer_class = OMC34Nivel3Serializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idOmc34N3 = pk).first()

    # def list(self, request):
    #     serializer = self.get_serializer(self.get_queryset(), many=True)
    #     return Response(serializer.data, status = status.HTTP_200_OK)
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response({'error':serializer.errors},status = status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe un Registro con estos datos!'}, status = status.HTTP_404_NOT_FOUND)

    def destroy(self,request,pk=None):
        registro = self.get_queryset().filter(idOmc34N3=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un Registro con estos datos!'}, status = status.HTTP_404_NOT_FOUND)

# TABLA OMNICLAS 34 Nivel 4
class OMC34Nivel4(viewsets.ModelViewSet):
    serializer_class = OMC34Nivel4Serializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idOmc34N4 = pk).first()

    # def list(self, request):
    #     serializer = self.get_serializer(self.get_queryset(), many=True)
    #     return Response(serializer.data, status = status.HTTP_200_OK)
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response({'error':serializer.errors},status = status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe un Registro con estos datos!'}, status = status.HTTP_404_NOT_FOUND)

    def destroy(self,request,pk=None):
        registro = self.get_queryset().filter(idOmc34N4=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un Registro con estos datos!'}, status = status.HTTP_404_NOT_FOUND)