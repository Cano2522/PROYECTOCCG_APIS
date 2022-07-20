from django.db import models
from datosgeograficos.models import CP

# Create your models here.

class Proveedor(models.Model):
    idProveedor = models.BigAutoField(auto_created=True,primary_key=True, serialize=False, verbose_name='idProveedor')
    Nombre = models.CharField(max_length=60, null=False)
    RFC = models.CharField(max_length=13, blank=True, null=True)
    Email = models.CharField(max_length=45, blank=True, null=True)
    Observaciones = models.CharField(max_length=500, blank=True, null=True)
    logoImg = models.ImageField('Logo', upload_to='proveedor/', max_length=255, blank=True, null=True)
    urlSitioWeb = models.CharField(max_length=70, blank=True, null=True)
    Fabricante = models.BooleanField(blank=True, null=True)
    Activo = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return f'{self.Nombre}'

    class Meta:
        db_table = 'Proveedor'

class Marca(models.Model):
    idMarca = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idMarca')
    Nombre = models.CharField(unique=True, max_length=45, null=False)
    Activo = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return f'{self.Nombre}'

    class Meta:
        db_table = 'Marca'

class SectorMercado(models.Model):
    idSecMer = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idSecMer')
    Nombre = models.CharField(max_length=40, null=False, unique=True)

    def __str__(self):
        return f'{self.Nombre}'

    class Meta:
        db_table = 'SectorMercado'


class ProveedorMarca(models.Model):
    idProvMar = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idProveedorMarca')
    fk_Proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE, db_column='fk_Proveedor', verbose_name='Proveedor')
    fk_Marca = models.ForeignKey(Marca,on_delete=models.CASCADE, db_column='fk_Marca', verbose_name='Marca')

    class Meta:
        db_table = 'ProveedorMarca'

class SucursalProv(models.Model):
    idSucProv = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idSucProv')
    Alias = models.CharField(max_length=80, null=False)
    numTel = models.CharField(max_length=20, null=False)
    contactoAten = models.CharField(max_length=50, null=False)
    nomSuperior = models.CharField(max_length=50, blank=True, null=True)
    cargoSuperior = models.CharField(max_length=50, blank=True, null=True)
    Calle = models.CharField(max_length=50, null=False)
    noInt = models.IntegerField(null=False)
    noExt = models.IntegerField(blank=True, null=True)
    Colonia = models.CharField(max_length=50, null=False)
    fk_CP = models.ForeignKey(CP,on_delete=models.CASCADE, db_column='fk_CP', verbose_name='CP')
    fk_Proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE, db_column='fk_Proveedor', verbose_name='Proveedor')

    def __str__(self):
        return f'{self.Nombre}'

    class Meta:
        db_table = 'SucursalProv'

class SectorProv(models.Model):
    idSecProv = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idSecProv')
    fk_Proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE, db_column='fk_Proveedor', verbose_name='Proveedor')
    fk_SecMer = models.ForeignKey(SectorMercado,on_delete=models.CASCADE, db_column='fk_SecMer', verbose_name='Sector Mercado')

    class Meta:
        db_table = 'SectorProv'