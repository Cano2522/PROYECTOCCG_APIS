from django.db import models

# Create your models here.

class TipoUniMed(models.Model):
    idTum = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idTum')
    Tipo = models.CharField(max_length=65, null=False)

    def __str__(self):
        return f'{self.Tipo}'

    class Meta:
        db_table = 'TipoUniMed'

class SubTipUni(models.Model):
    idStu = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idStu')
    Subtipo = models.CharField(max_length=200, null=False)
    fk_Tum = models.ForeignKey(TipoUniMed, on_delete=models.CASCADE, db_column='fk_Tum', verbose_name='Tipo Unidad de Medida')

    def __str__(self):
        return f'{self.Subtipo}'

    class Meta:
        db_table = 'subtipUni'

class UnidadesMedida(models.Model):
    idUniMed = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idUniMed')
    cveSat = models.CharField(max_length=50,blank=True,null=True)
    Unidad = models.CharField(max_length=50,null=False, unique=True)
    Descripcion = models.CharField(max_length=80,null=False)
    Sistema = models.CharField(max_length=30,blank=True,null=True)
    fk_Stu = models.ForeignKey(SubTipUni, on_delete=models.CASCADE, db_column='fk_Stu', verbose_name='Subtipo Unidad de Medida')

    def __str__(self):
        return f'{self.Unidad}'

    class Meta:
        db_table = 'UnidadesMedida'