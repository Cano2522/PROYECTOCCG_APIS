from django.db import connection
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from usuarios.authentication_mixins import Authentication
from rolesorg.serializers import RolesOrgSerializer

# Create your views here.
class RolesOrg(Authentication,viewsets.ModelViewSet):
    serializer_class = RolesOrgSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idRolOrg=pk).first()
    
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
        return Response({'error':'No existe un registro con esos datos'}, status = status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        registro = self.get_queryset(pk)
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un registro con estos datos'}, status = status.HTTP_404_NOT_FOUND)

class ListarRolesXOMC23N2(Authentication,viewsets.GenericViewSet):
    def get_queryset(self):
        with connection.cursor() as cursor:
            registros = cursor.execute("SELECT Omc34Nivel2 .codigo,Omc34Nivel2.descriEng AS descriEngOMC,Omc34Nivel2.descriSpa AS descriSpaOMC,Omc34Nivel2.anioReg,Omc34Nivel2.regFinal,RolesOrg.codigo AS codigoOmc,RolesOrg.consecutivo,RolesOrg.descriEng AS descriEngRol,RolesOrg.descriSpa AS descriSpaRol,RolesOrg.definicionEng,RolesOrg.definicionSpa,RolesOrg.fuenteInf,RolesOrg.fecRegInf FROM Omc34Nivel2 JOIN RolesOrg ON Omc34Nivel2.codigo=RolesOrg.codigo")
            registros = dictfetchall(cursor)
            return registros
        
    def list(self, request):
        data = self.get_queryset()
        if data:
            return Response(data, status = status.HTTP_200_OK)
        else:
            return Response({'mensaje':'No existen registros'}, status = status.HTTP_404_NOT_FOUND)

class ListarRolesXOMC23N3(Authentication,viewsets.GenericViewSet):
    def get_queryset(self):
        with connection.cursor() as cursor:
            registros = cursor.execute("SELECT Omc34Nivel3.codigo,Omc34Nivel3.descriEng AS descriEngOMC,Omc34Nivel3.descriSpa AS descriSpaOMC,Omc34Nivel3.anioReg,Omc34Nivel3.regFinal,RolesOrg.codigo AS codigoOmc,RolesOrg.consecutivo,RolesOrg.descriEng AS descriEngRol,RolesOrg.descriSpa AS descriSpaRol,RolesOrg.definicionEng,RolesOrg.definicionSpa,RolesOrg.fuenteInf,RolesOrg.fecRegInf FROM Omc34Nivel3 JOIN RolesOrg ON Omc34Nivel3.codigo=RolesOrg.codigo")
            registros = dictfetchall(cursor)
            return registros
        
    def list(self, request):
        data = self.get_queryset()
        if data:
            return Response(data, status = status.HTTP_200_OK)
        else:
            return Response({'mensaje':'No existen registros'}, status = status.HTTP_404_NOT_FOUND)

class ListarRolesXOMC23N4(Authentication,viewsets.GenericViewSet):
    def get_queryset(self):
        with connection.cursor() as cursor:
            registros = cursor.execute("SELECT Omc34Nivel4.codigo,Omc34Nivel4.descriEng AS descriEngOMC,Omc34Nivel4 .descriSpa AS descriSpaOMC,Omc34Nivel4.anioReg,Omc34Nivel4.regFinal,RolesOrg.codigo AS codigoOmc,RolesOrg.consecutivo,RolesOrg.descriEng AS descriEngRol,RolesOrg.descriSpa AS descriSpaRol,RolesOrg.definicionEng,RolesOrg.definicionSpa,RolesOrg.fuenteInf,RolesOrg.fecRegInf FROM Omc34Nivel4 JOIN RolesOrg ON Omc34Nivel4.codigo=RolesOrg.codigo")
            registros = dictfetchall(cursor)
            return registros
        
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
