from rest_framework import serializers 
from materiales.models import (
    Materiales,
    Concreto,
    CaracEspe,
    Esfuerzo,
    ValorEsfuerzo,
    TipoResistencia,
    ApliPrincipales,
    TMA,
    Revenimiento,
    Densidad,
    SistColocacion,
    ClasExposicion,
    FlujoRev,
    IonCloruro,
    FibraConcre,
)
        
#SERIALIZERS CORRESPONDIENTES A ENTIDADES RELACIONADAS A MATERIALES

class MaterialesSerializer(serializers.ModelSerializer):  #ESTE ME DEBERIA SERVIR PARA GENERAR EL CONSECUTIVO
    class Meta:
        model = Materiales
        fields = ['idMaterial','numMat','codigoOmc','consecutivo','descriCorta','descriLarga','comentarios','palabrasCve','desCorEng','desLargEng','fuenteInf','fecRegInf','codigoBimsa']

class ConcretoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concreto
        fields = ['idConcreto','numMat','codigo','fk_Material','fk_ClasExpo','fk_SistColoc','fk_Densidad','fk_Reven','fk_FlujoRev','fk_FibraConcre','fk_ValEsf','fk_Tma','fk_AplPrinc']

class CaracEspeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaracEspe
        fields = ['idCaracEspec','modElast','acronimo1','edad','absorcionCap','acronimo2','trabaExtend','clase','color','comportamiento','conAire','conIonClor','tiempoPrueba','fk_IonClor','fk_Concreto']

class EsfuerzoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Esfuerzo
        fields = ['idEsfuerzo','tipoEsfuerzo','fk_Acronimo']

class ValorEsfuerzoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValorEsfuerzo
        fields = ['idValEsf','valor','fk_Esfuerzo','fk_UniMed','fk_TipoResist']

class TipoResistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoResistencia
        fields = ['idTipoResist','tipo']

class AplPrincipalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApliPrincipales
        fields = ['idApliPrincipales','aplicaciones']

class TMASerializer(serializers.ModelSerializer):
    class Meta:
        model = TMA
        fields = ['idTma','valTma','tmaFrac','fk_UniMed','fk_Acronimo']

class RevenimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revenimiento
        fields = ['idReven','valRev','fk_Acronimo','fk_UniMed','fk_TipoCons']

class DensidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Densidad
        fields = ['idDensidad','denRelativa','denRelatAparent','valDensidad','denAparente','unidadPeso','unidadPesoSss','fk_UniMed']

class SistColocacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SistColocacion
        fields = ['idSistColoc','tipoSistema']

class ClasExposicionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClasExposicion
        fields = ['idClasExpo','categoria','condicion','clase','fk_AguaCem','fk_ValEsf']

class FlujoRevSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlujoRev
        fields = ['idFlujoRev','valFluRev','fk_UniMed']

class IonCloruroSerializer(serializers.ModelSerializer):
    class Meta:
        model = IonCloruro
        fields = ['idIonClor','cargaPesada','tipoPenet']

class FibraConcreSerializer(serializers.ModelSerializer):
    class Meta:
        model = FibraConcre
        fields = ['idFibraCon','tipo','tipoMaterial','fibras']
