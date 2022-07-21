from django.db import connection
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from materiales.serializers import (
    MaterialesSerializer,
    ConcretoSerializer,
    CaracEspeSerializer,
    EsfuerzoSerializer,
    ValorEsfuerzoSerializer,
    TipoResistenciaSerializer,
    AplPrincipalesSerializer,
    TMASerializer,
    RevenimientoSerializer,
    DensidadSerializer,
    SistColocacionSerializer,
    ClasExposicionSerializer,
    FlujoRevSerializer,
    IonCloruroSerializer,
    FibraConcreSerializer,
)
# Create your views here.

#TABLAS OMNICLAS 35 NIVEL 1
class VistaMaterial(viewsets.ModelViewSet):
    serializer_class = MaterialesSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idMaterial = pk).first()

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
        return Response({'error':'No existe un Registro con esos datos'}, status = status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk=None):
        registro = self.get_queryset().filter(idMaterial=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un Registro con estos datos!'}, status = status.HTTP_404_NOT_FOUND)

class VistaConcreto(viewsets.ModelViewSet):
    serializer_class = ConcretoSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idConcreto = pk).first()

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
        return Response({'error':'No existe un Registro con esos datos'}, status = status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk=None):
        registro = self.get_queryset().filter(idConcreto=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un Registro con estos datos!'}, status = status.HTTP_404_NOT_FOUND)

class VistaCaracEspe(viewsets.ModelViewSet):
    serializer_class = CaracEspeSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idCaracEspec = pk).first()

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
        return Response({'error':'No existe un Registro con esos datos'}, status = status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk=None):
        registro = self.get_queryset().filter(idCaracEspec=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un Registro con estos datos!'}, status = status.HTTP_404_NOT_FOUND)

class VistaEsfuerzo(viewsets.ModelViewSet):
    serializer_class = EsfuerzoSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idEsfuerzo = pk).first()

class VistaValorEsfuerzo(viewsets.ModelViewSet):
    serializer_class = ValorEsfuerzoSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idValEsf = pk).first()

class VistaTipoResistencia(viewsets.ModelViewSet):
    serializer_class = TipoResistenciaSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idTipoResist = pk).first()

class VistaAplPrincipales(viewsets.ModelViewSet):
    serializer_class = AplPrincipalesSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idAplPrinc = pk).first()

class VistaTMA(viewsets.ModelViewSet):
    serializer_class = TMASerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idTma = pk).first()

class VistaRevenimiento(viewsets.ModelViewSet):
    serializer_class = RevenimientoSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idReven = pk).first()

class VistaDensidad(viewsets.ModelViewSet):
    serializer_class = DensidadSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idDensidad = pk).first()

class VistaSistColocacion(viewsets.ModelViewSet):
    serializer_class = SistColocacionSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idSistColoc = pk).first()

class VistaClasExposicion(viewsets.ModelViewSet):
    serializer_class = ClasExposicionSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idClasExpo = pk).first()

class VistaFlujoRev(viewsets.ModelViewSet):
    serializer_class = FlujoRevSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idFlujoRev = pk).first()

class VistaIonCloruro(viewsets.ModelViewSet):
    serializer_class = IonCloruroSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idIonClor = pk).first()

class VistaFibraConcre(viewsets.ModelViewSet):
    serializer_class = FibraConcreSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idFibraCon = pk).first()

class ListarConcretosMateriales(viewsets.GenericViewSet):
    def get_queryset(self):
         with connection.cursor() as cursor:
            listarConcreto = cursor.execute("SELECT Mat.codigoOmc, Mat.Consecutivo,Mat.descriCorta,Mat.descriLarga,Mat.Comentarios,Mat.palabrasCve,Mat.desCorEng,Mat.desLargEng,Mat.fuenteInf,Mat.fecRegInf,Mat.codigoBimsa,Omc23Nivel3.descriSpa AS Nombre,acroEsf.Sigla, ValorEsfuerzo.Valor AS ValorEsfuerzo,uniVal.Unidad,Esfuerzo.tipoEsfuerzo,TipoResistencia.Tipo AS TipoResistencia,acroTma.Sigla,TMA.valTma,acroRev.Sigla,Tma.tmaFrac,Revenimiento.valRev,uniRev.Unidad,TipoConsistencia.Tipo AS TipoCons, CaracEspe.modElast,CaracEspe.Acronimo,CaracEspe.Edad,CaracEspe.absorcionCap,CaracEspe.Acronimo2,CaracEspe.trabaExtend,CaracEspe.Clase,CaracEspe.Color,CaracEspe.Comportamiento,CaracEspe.conAire,CaracEspe.conIonClor,CaracEspe.tiempoPrueba,SistColocacion.tipoSistema FROM Omc23Nivel3 FULL JOIN  Materiales mat ON mat.codigoOmc=Omc23Nivel3.Codigo FULL JOIN  Concreto ON fk_Material=idMaterial FULL JOIN Revenimiento ON fk_Reven=idReven FULL JOIN Acronimo acroRev ON Revenimiento.fk_Acronimo=acroRev.idAcronimo FULL  JOIN UnidadesMedida uniRev ON Revenimiento.fk_UniMed=uniRev.idUniMed FULL JOIN ValorEsfuerzo ON fk_ValEsf=idValEsf JOIN Esfuerzo ON Esfuerzo.idEsfuerzo=ValorEsfuerzo.fk_Esfuerzo JOIN UnidadesMedida uniVal ON uniVal.idUniMed=ValorEsfuerzo.fk_UniMed FULL JOIN Acronimo acroEsf ON Esfuerzo.fk_Acronimo=acroEsf.idAcronimo FULL JOIN TMA ON fk_Tma=idTma FULL JOIN Acronimo acroTma ON Tma.fk_Acronimo=acroTma.idAcronimo FULL JOIN SistColocacion ON fk_SistColoc=idSistColoc FULL JOIN TipoConsistencia ON Revenimiento.fk_TipoCons=TipoConsistencia.idTipoCons FULL JOIN TipoResistencia ON TipoResistencia.idTipoResist=ValorEsfuerzo.fk_TipoResist FULL JOIN CaracEspe ON fk_Concreto=idConcreto  WHERE codigoOmc is not null")
            listarConcreto =dictfetchall(cursor)
            return listarConcreto
        
    
    def list(self,request):
        data = self.get_queryset()
        if data:
            return Response(data, status = status.HTTP_200_OK)
        else:
            return Response({'mensaje':'No existe un Registro!'}, status = status.HTTP_404_NOT_FOUND)


def dictfetchall(cursor): 
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]