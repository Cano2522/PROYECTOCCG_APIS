from django.shortcuts import render
from django.db import connection
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from usuarios.authentication_mixins import Authentication

# Create your views here.

class ListarAcerosRefuerzo(Authentication,viewsets.GenericViewSet):
    def get_queryset(self):
        with connection.cursor() as cursor:
            registros = cursor.execute("SELECT Materiales.codigoOmc AS CodigoOmc23,Materiales.Consecutivo,Materiales.descriCorta,Materiales.descriLarga,Materiales.Comentarios,Materiales.palabrasCve,Materiales.desCorEng,Materiales.desLargEng,Materiales.fuenteInf,Materiales.fecRegInf,Materiales.codigoBimsa,Omc23Nivel5.descriSpa AS Omniclass,Grado.valorGrad,Dimensiones.noVarilla,Dimensiones.diametro,Dimensiones.area,Dimensiones.perimetro,Dimensiones.masa,Esfuerzo.tipoEsfuerzo FROM Omc23Nivel5 JOIN  Materiales ON codigoOmc=Omc23Nivel5.Codigo JOIN AceroRefuerzo ON fk_Material=idMaterial JOIN Grado ON idGrado=fk_Grado JOIN Dimensiones ON fk_Dimensiones=idDimensiones JOIN Esfuerzo ON Esfuerzo.idEsfuerzo=AceroRefuerzo.fk_Esfuerzo")
            registros = dictfetchall(cursor)
            return registros
        
    def list(self, request):
        data = self.get_queryset()
        if data:
            return Response(data, status = status.HTTP_200_OK)
        else:
            return Response({'mensaje':'No existen registros'}, status = status.HTTP_404_NOT_FOUND)

class ListarCementos(Authentication,viewsets.GenericViewSet):
    def get_queryset(self):
        with connection.cursor() as cursor:
            registros = cursor.execute("SELECT Materiales.codigoOmc AS CodigoOmc23,Materiales.Consecutivo,Materiales.descriCorta,Materiales.descriLarga,Materiales.Comentarios,Materiales.palabrasCve,Materiales.desCorEng,Materiales.desLargEng,Materiales.fuenteInf,Materiales.fecRegInf,Materiales.codigoBimsa,Omc23Nivel5.descriSpa AS Omniclass,ClasifCemento.tipo,ClaseResist.clase FROM Omc23Nivel5 JOIN  Materiales ON codigoOmc=Omc23Nivel5.Codigo JOIN Cemento ON fk_Material=idMaterial JOIN ClaseResist ON fk_ClasRe=idClasRes JOIN ClasifCemento ON fk_ClasCem=idClasCem")
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
