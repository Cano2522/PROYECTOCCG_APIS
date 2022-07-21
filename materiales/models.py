from django.db import models
from unidadesmedida.models import UnidadesMedida

# Create your models here.
#ENTIDADES CORRESPONDIENTES A "MATERIALES"

class TipoResistencia(models.Model):
    idTipoResist = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idTipoResist')
    Tipo = models.CharField(max_length=30, null=False)

    def __str__(self):
        return f'{self.Tipo}'

    class Meta:
        db_table = "TipoResistencia"

class AplPrincipales(models.Model):
    idAplPrinc = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idAplPrinc')
    aplicaciones = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f'{self.aplicaciones}'

    class Meta:
        db_table = "AplPrincipales"

class SistColocacion(models.Model):
    idSistColoc = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idSistColoc')
    tipoSistema = models.CharField(max_length=30, null=False)

    def __str__(self):
        return f'{self.tipoSistema}'

    class Meta:
        db_table = "SistColocacion"

class FibraConcre(models.Model):
    idFibraCon = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idFibraCon')
    Tipo = models.CharField(max_length=20, null=False)
    tipoMaterial = models.CharField(max_length=20, null=False)
    Fibras = models.CharField(max_length=20, null=False)

    def __str__(self):
        return f'{self.Fibras}'

    class Meta:
        db_table = 'FibraConcre'

class Acronimo(models.Model):
    idAcronimo = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idAcronimo')
    Sigla = models.CharField(max_length=15, null=False)
    Descripcion = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return f'{self.Sigla}'

    class Meta:
        db_table = 'Acronimo'

class TipoConsistencia(models.Model):
    idTipoCons = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idTipoCons')
    Tipo = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.Tipo}'

    class Meta:
        db_table = 'TipoConsistencia'

class Esfuerzo(models.Model):
    idEsfuerzo = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idEsfuerzo')
    tipoEsfuerzo = models.CharField(max_length=50, null=False)
    fk_Acronimo = models.ForeignKey(Acronimo, on_delete=models.CASCADE, db_column='fk_Acronimo', verbose_name='Acronimo')

    def __str__(self):
        return f'{self.tipoEsfuerzo}'
    
    class Meta:
        db_table = 'Esfuerzo'

class ValorEsfuerzo(models.Model):
    idValEsf = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idValEsf')
    Valor = models.FloatField(null=False)
    fk_Esfuerzo = models.ForeignKey(Esfuerzo, on_delete=models.CASCADE, db_column='fk_Esfuerzo', verbose_name='Esfuerzo')
    fk_UniMed = models.ForeignKey(UnidadesMedida, on_delete=models.CASCADE, db_column='fk_UniMed', verbose_name='Unidad Medida')
    fk_TipoResist = models.ForeignKey(TipoResistencia, on_delete=models.SET_NULL, blank=True, null=True, db_column='fk_TipoResist')

    def __str__(self):
        return f'{self.Valor}'

    class Meta:
        db_table = 'ValorEsfuerzo'

class TMA(models.Model):
    idTma = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idTma')
    valTma = models.CharField(max_length=5, null=False)
    tmaFrac = models.CharField(max_length=8, blank=True, null=True)
    fk_UniMed = models.ForeignKey(UnidadesMedida, on_delete=models.CASCADE, db_column='fk_UniMed', verbose_name='Unidad Medida')
    fk_Acronimo = models.ForeignKey(Acronimo, on_delete=models.SET_NULL, blank=True, null=True, db_column='fk_Acronimo', verbose_name='Acronimo')

    def __str__(self):
        return f'{self.valTma}'

    class Meta:
        db_table = 'TMA'

class Revenimiento(models.Model):
    idReven = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idReven')
    valRev = models.CharField(max_length=10, null=False)
    fk_Acronimo = models.ForeignKey(Acronimo, on_delete=models.CASCADE, db_column='fk_Acronimo', verbose_name='Acronimo')
    fk_UniMed = models.ForeignKey(UnidadesMedida, on_delete=models.CASCADE, db_column='fk_UniMed', verbose_name='Unidad Medida')
    fk_TipoCons = models.ForeignKey(TipoConsistencia, on_delete=models.SET_NULL, blank=True, null=True, db_column='fk_TipoCons', verbose_name='Tipo Consistencia')

    def __str__(self):
        return f'{self.valRev}'

    class Meta:
        db_table = 'Revenimiento'

class Densidad(models.Model):
    idDensidad = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idDensidad')
    denRelativa = models.FloatField(blank=True, null=True)
    denRelatAparent = models.FloatField(blank=True, null=True)
    valDensidad = models.FloatField(null=False)
    denAparente = models.FloatField(blank=True, null=True)
    unidadPeso = models.FloatField(blank=True, null=True)
    unidadPesoSss = models.FloatField(blank=True, null=True)
    fk_UniMed = fk_UniMed = models.ForeignKey(UnidadesMedida, on_delete=models.CASCADE, db_column='fk_UniMed', verbose_name='Unidad Medida')

    def __str__(self):
        return f'{self.valDensidad}'

    class Meta:
        db_table = 'Densidad'

class AguaCemento(models.Model):
    idAguaCem = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idAguaCem')
    relacionAc = models.CharField(max_length=5, null=False)
    fk_Acronimo = models.ForeignKey(Acronimo, on_delete=models.CASCADE, db_column='fk_Acronimo', verbose_name='Acronimo')

    def __str__(self):
        return f'{self.relacionAc}'

    class Meta:
        db_table = 'AguaCemento'

class ClasExposicion(models.Model):
    idClasExpo = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idClasExpo')
    Categoria = models.CharField(max_length=60, null=False)
    Condicion = models.CharField(max_length=600, null=False)
    Clase = models.CharField(max_length=2, null=False)
    fk_AguaCem = models.ForeignKey(AguaCemento, on_delete=models.CASCADE, db_column='fk_AguaCem', verbose_name='Agua Cemento')
    fk_ValEsf = models.ForeignKey(ValorEsfuerzo, on_delete=models.CASCADE, db_column='fk_ValEsf', verbose_name='Valor Esfuerzo')

    def __str__(self):
        return f'{self.Clase}'

    class Meta:
        db_table = 'ClasExposicion'

class FlujoRev(models.Model):
    idFlujoRev = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idFlujoRev')
    valFluRev = models.FloatField(null=False)
    fk_UniMed = models.ForeignKey(UnidadesMedida, on_delete=models.CASCADE, db_column='fk_UniMed', verbose_name='Unidad Medida')

    def __str__(self):
        return f'{self.valFluRev}'

    class Meta:
        db_table = 'FlujoRev'

class IonCloruro(models.Model):
    idIonClor = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idIonClor')
    cargaPesada = models.CharField(max_length=15, null=False)
    tipoPenet = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f'{self.cargaPesada}'

    class Meta:
        db_table = 'IonCloruro'

class Materiales(models.Model):
    idMaterial = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idMaterial')
    numMat = models.IntegerField(null=False)
    codigoOmc = models.CharField(max_length=18, null=False)
    Consecutivo = models.CharField(max_length=5,blank=True, null=True)
    descriCorta = models.CharField(max_length=100, blank=True, null=True)
    descriLarga = models.TextField(blank=True, null=True)
    Comentarios = models.CharField(max_length=200, blank=True, null=True)
    palabrasCve = models.CharField(max_length=45, blank=True, null=True)
    desCorEng = models.CharField(max_length=100, blank=True, null=True)
    desLargEng = models.TextField(blank=True, null=True)
    fuenteInf = models.CharField(max_length=45, null=False)
    fecRegInf = models.DateField(null=False)
    codigoBimsa = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f'{self.codigoOmc}: {self.descriCorta}'

    class Meta:
        db_table = "Materiales"

#CONCRETO

class Concreto(models.Model):
    idConcreto = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idConcreto')
    numMat = models.IntegerField(null=False)
    Codigo = models.CharField(max_length=18, null=False)
    fk_Material = models.ForeignKey(Materiales, on_delete=models.CASCADE,db_column='fk_Material', verbose_name='Materiales')
    fk_ClasExpo = models.ForeignKey(ClasExposicion, on_delete=models.SET_NULL, blank=True, null=True, db_column='fk_ClasExpo', verbose_name='Clase Exposicion')
    fk_SistColoc = models.ForeignKey(SistColocacion, on_delete=models.CASCADE,db_column='fk_SistColoc', verbose_name='Sistema Colocacion')
    fk_Densidad = models.ForeignKey(Densidad, on_delete=models.SET_NULL, blank=True, null=True, db_column='fk_Densidad', verbose_name='Densidad')
    fk_Reven = models.ForeignKey(Revenimiento, on_delete=models.CASCADE,db_column='fk_Reven', verbose_name='Revenimiento')
    fk_FlujoRev = models.ForeignKey(FlujoRev, on_delete=models.SET_NULL, blank=True, null=True, db_column='fk_FlujoRev', verbose_name='Flujo Revenimiento')
    fk_FibraConcre = models.ForeignKey(FibraConcre, on_delete=models.SET_NULL, blank=True, null=True, db_column='fk_FibraConcre', verbose_name='Fibra')
    fk_ValEsf = models.ForeignKey(ValorEsfuerzo, on_delete=models.CASCADE,db_column='fk_ValEsf', verbose_name='Valor Esfuerzo')
    fk_Tma = models.ForeignKey(TMA, on_delete=models.CASCADE,db_column='fk_Tma', verbose_name='TMA')
    fk_AplPrinc = models.ForeignKey(AplPrincipales, on_delete=models.SET_NULL, blank=True, null=True, db_column='fk_AplPrinc', verbose_name='Aplicaciones Principales')
    

    def __str__(self):
        return f'{self.Codigo}'

    class Meta:
        db_table = "Concreto"

class CaracEspe(models.Model):
    idCaracEspec = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idCaracEspec')
    modElast = models.FloatField(blank=True, null=True)
    Acronimo = models.CharField(max_length=3, blank=True, null=True)
    Edad = models.FloatField(blank=True, null=True)
    absorcionCap = models.FloatField(blank=True, null=True)
    Acronimo2 = models.CharField(max_length=3, blank=True, null=True)
    trabaExtend = models.FloatField(blank=True, null=True)
    Clase = models.CharField(max_length=10, blank=True, null=True)
    Color = models.CharField(max_length=10, blank=True, null=True)
    Comportamiento = models.CharField(max_length=30, blank=True, null=True)
    conAire = models.FloatField(blank=True, null=True)
    conIonClor = models.FloatField(blank=True, null=True)
    tiempoPrueba = models.FloatField(blank=True, null=True)
    fk_IonClor = models.ForeignKey(IonCloruro, on_delete=models.SET_NULL, blank=True, null=True, db_column='fk_IonClor', verbose_name='Ion Cloruro')
    fk_Concreto = models.ForeignKey(Concreto, on_delete=models.SET_NULL, blank=True, null=True, db_column='fk_Concreto', verbose_name='Concreto')

    def __str__(self):
        return f'{self.idCaracEspec}: {self.Acronimo}'

    class Meta:
        db_table = "CaracEspe"
