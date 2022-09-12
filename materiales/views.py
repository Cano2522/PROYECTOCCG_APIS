from django.db import connection
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from usuarios.authentication_mixins import Authentication
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
    ClaseResistSerializer,
    ClasifCementoSerializer,
    CementoSerializer,
    GradoSerializer,
    DimensionesSerializer,
    AceroRefuerzoSerializer
)
# Create your views here.

#TABLAS OMNICLAS 35 NIVEL 1
class VistaMaterial(Authentication,viewsets.ModelViewSet):
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
            return Response({'mensaje':'Registro creado','data':serializer.data},status = status.HTTP_201_CREATED)
        return Response({'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'mensaje':'Registro actualizado','data':serializer.data}, status=status.HTTP_200_OK)
            return Response({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe un registro con esos datos'}, status = status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk=None):
        registro = self.get_queryset().filter(idMaterial=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un registro con estos datos!'}, status = status.HTTP_404_NOT_FOUND)

class VistaConcreto(Authentication,viewsets.ModelViewSet):
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
            return Response({'mensaje':'Registro creado','data':serializer.data},status = status.HTTP_201_CREATED)
        return Response({'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'mensaje':'Registro actualizado','data':serializer.data}, status=status.HTTP_200_OK)
            return Response({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe un registro con esos datos'}, status = status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk=None):
        registro = self.get_queryset().filter(idConcreto=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un registro con estos datos!'}, status = status.HTTP_404_NOT_FOUND)

class VistaCaracEspe(Authentication,viewsets.ModelViewSet):
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
            return Response({'mensaje':'Registro creado','data':serializer.data},status = status.HTTP_201_CREATED)
        return Response({'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'mensaje':'Registro actualizado','data':serializer.data}, status=status.HTTP_200_OK)
            return Response({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe un registro con esos datos'}, status = status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk=None):
        registro = self.get_queryset().filter(idCaracEspec=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un registro con estos datos!'}, status = status.HTTP_404_NOT_FOUND)

class VistaEsfuerzo(Authentication,viewsets.ModelViewSet):
    serializer_class = EsfuerzoSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idEsfuerzo = pk).first()

class VistaValorEsfuerzo(Authentication,viewsets.ModelViewSet):
    serializer_class = ValorEsfuerzoSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idValEsf = pk).first()

class VistaTipoResistencia(Authentication,viewsets.ModelViewSet):
    serializer_class = TipoResistenciaSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idTipoResist = pk).first()

class VistaAplPrincipales(Authentication,viewsets.ModelViewSet):
    serializer_class = AplPrincipalesSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idApliPrincipales = pk).first()

class VistaTMA(Authentication,viewsets.ModelViewSet):
    serializer_class = TMASerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idTma = pk).first()

class VistaRevenimiento(Authentication,viewsets.ModelViewSet):
    serializer_class = RevenimientoSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idReven = pk).first()

class VistaDensidad(Authentication,viewsets.ModelViewSet):
    serializer_class = DensidadSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idDensidad = pk).first()

class VistaSistColocacion(Authentication,viewsets.ModelViewSet):
    serializer_class = SistColocacionSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idSistColoc = pk).first()

class VistaClasExposicion(Authentication,viewsets.ModelViewSet):
    serializer_class = ClasExposicionSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idClasExpo = pk).first()

class VistaFlujoRev(Authentication,viewsets.ModelViewSet):
    serializer_class = FlujoRevSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idFlujoRev = pk).first()

class VistaIonCloruro(Authentication,viewsets.ModelViewSet):
    serializer_class = IonCloruroSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idIonClor = pk).first()

class VistaFibraConcre(Authentication,viewsets.ModelViewSet):
    serializer_class = FibraConcreSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idFibraCon = pk).first()

class ListarConcretosMateriales(Authentication,viewsets.GenericViewSet):
    def get_queryset(self):
         with connection.cursor() as cursor:
            listarConcreto = cursor.execute("SELECT Mat.idMaterial,Mat.codigoOmc, Mat.consecutivo,Mat.descriCorta,Mat.descriLarga,Mat.comentarios,Mat.palabrasCve,Mat.desCorEng,Mat.desLargEng,Mat.fuenteInf,Mat.fecRegInf,Mat.codigoBimsa,Omc23Nivel3.descriSpa AS nombre,acroEsf.sigla as siglaEsf,ValorEsfuerzo.valor AS valorEsfuerzo,uniVal.unidad AS unidadEsf,Esfuerzo.tipoEsfuerzo,TipoResistencia.tipo AS tipoResistencia,acroTma.sigla AS siglaTma,TMA.valTma,acroRev.sigla as siglaRev,Tma.tmaFrac,Revenimiento.valRev,uniRev.unidad AS unidadRev,TipoConsistencia.Tipo AS tipoCons,CaracEspe.modElast,CaracEspe.acronimo1,CaracEspe.edad,CaracEspe.absorcionCap,CaracEspe.acronimo2,CaracEspe.trabaExtend,CaracEspe.clase,CaracEspe.color,CaracEspe.comportamiento,CaracEspe.conAire,CaracEspe.conIonClor,CaracEspe.tiempoPrueba,SistColocacion.tipoSistema FROM Omc23Nivel3 FULL JOIN  Materiales mat ON mat.codigoOmc=Omc23Nivel3.Codigo FULL JOIN  Concreto ON fk_Material=idMaterial FULL JOIN Revenimiento ON fk_Reven=idReven FULL JOIN Acronimo acroRev ON Revenimiento.fk_Acronimo=acroRev.idAcronimo FULL  JOIN UnidadesMedida uniRev ON Revenimiento.fk_UniMed=uniRev.idUniMed FULL JOIN ValorEsfuerzo ON fk_ValEsf=idValEsf JOIN Esfuerzo ON Esfuerzo.idEsfuerzo=ValorEsfuerzo.fk_Esfuerzo JOIN UnidadesMedida uniVal ON uniVal.idUniMed=ValorEsfuerzo.fk_UniMed FULL JOIN Acronimo acroEsf ON Esfuerzo.fk_Acronimo=acroEsf.idAcronimo FULL JOIN TMA ON fk_Tma=idTma FULL JOIN Acronimo acroTma ON Tma.fk_Acronimo=acroTma.idAcronimo FULL JOIN SistColocacion ON fk_SistColoc=idSistColoc FULL JOIN TipoConsistencia ON Revenimiento.fk_TipoCons=TipoConsistencia.idTipoCons FULL JOIN TipoResistencia ON TipoResistencia.idTipoResist=ValorEsfuerzo.fk_TipoResist FULL JOIN CaracEspe ON fk_Concreto=idConcreto WHERE codigoOmc IS NOT NULL")
            listarConcreto =dictfetchall(cursor)
            return listarConcreto
    
    def list(self,request):
        data = self.get_queryset()
        if data:
            return Response(data, status = status.HTTP_200_OK)
        else:
            return Response({'mensaje':'No existe un registro'}, status = status.HTTP_404_NOT_FOUND)

# FUNCIONES CORRESPONDIENTES A CEMENTOS
class VistaCemento(Authentication,viewsets.ModelViewSet):
    serializer_class = CementoSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idCemento = pk).first()

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
        return Response({'error':'No existe un registro con esos datos'}, status = status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk=None):
        registro = self.get_queryset().filter(idCemento=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un registro con estos datos!'}, status = status.HTTP_404_NOT_FOUND)

class VistaClaseResist(Authentication,viewsets.ModelViewSet):
    serializer_class = ClaseResistSerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idClasRes = pk).first()

class VistaClasifCemento(Authentication,viewsets.ModelViewSet):
    serializer_class = ClasifCementoSerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idClasRes = pk).first()

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

# FUNCIONES CORRESPONDIENTES A ACERO REFORZADO
class VistaAceroRefuerzo(Authentication,viewsets.ModelViewSet):
    serializer_class = AceroRefuerzoSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idAceroRef = pk).first()

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
        return Response({'error':'No existe un registro con esos datos'}, status = status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk=None):
        registro = self.get_queryset().filter(idAceroRef=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un registro con estos datos!'}, status = status.HTTP_404_NOT_FOUND)

class VistaDimensiones(Authentication,viewsets.ModelViewSet):
    serializer_class = DimensionesSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idDimensiones = pk).first()

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
        return Response({'error':'No existe un registro con esos datos'}, status = status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk=None):
        registro = self.get_queryset().filter(idDimensiones=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un registro con estos datos!'}, status = status.HTTP_404_NOT_FOUND)

class VistaGrado(Authentication,viewsets.ModelViewSet):
    serializer_class = GradoSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idGrado = pk).first()

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

class ListarMaterialContratista(Authentication,viewsets.GenericViewSet):
    def get_queryset(self):
        with connection.cursor() as cursor:
            registros = cursor.execute("SELECT * FROM vw_materialContratista")
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