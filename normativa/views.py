from django.db import connection
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from usuarios.authentication_mixins import Authentication

from normativa.serializers import NormativaSerializer

# Create your views here.

class VistaNormativa(Authentication,viewsets.ModelViewSet):
    serializer_class = NormativaSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idNormativa=pk).first()

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensaje':'Registro creado','data':serializer.data}, status = status.HTTP_201_CREATED)
        return Response({'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data= request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'mensaje':'Registro actualizado','data':serializer.data}, status = status.HTTP_200_OK)
            return Response({'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe registro con esos datos'}, status = status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        serializer = self.get_queryset(pk)
        if serializer:
            serializer.delete()
            return Response({'mensaje':'Registro eliminado correctamente'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un registro con estos datos'}, status = status.HTTP_404_NOT_FOUND)


class ListarNormativaAcronimo(Authentication, viewsets.GenericViewSet):
    def get_queryset(self):
        with connection.cursor() as cursor:
            registro = cursor.execute('SELECT idNormativa, nombreSpa,nombreEng,sigla FROM Normativa JOIN Acronimo ON fk_Acronimo=idAcronimo')
            registro = dictfetchall(cursor)
            return registro
    
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