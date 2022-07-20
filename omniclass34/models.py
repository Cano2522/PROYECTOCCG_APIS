from django.db import models

# Create your models here.
class OMC34Nivel1(models.Model):
    idOmc34N1 = models.BigAutoField(auto_created=True, primary_key= True, serialize= False, verbose_name='idOmc34N1')
    Codigo = models.CharField(max_length=9, null=False)
    descriEng = models.CharField(max_length=30, null= False)
    descriSpa = models.CharField(max_length=30, null= False)
    definicionEng = models.CharField(max_length=200, null= False)
    definicionSpa = models.CharField(max_length=200, null= False)
    anioReg = models.IntegerField(null=False)

    def __str__(self):
        return f'{self.Codigo}: {self.descriSpa}'

    class Meta:
        db_table = "Omc34Nivel1"

class OMC34Nivel2(models.Model):
    idOmc34N2 = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idOmc34N2')
    # cveRol = models.IntegerField(blank=True, null=True)
    Codigo = models.CharField(max_length=9, null=False)
    descriEng = models.CharField(max_length=35, null=False)
    descriSpa = models.CharField(max_length=50, null=False)
    definicionEng = models.CharField(max_length=300, null=False)
    definicionSpa = models.CharField(max_length=300, null=False)
    anioReg = models.IntegerField(null=False)
    regFinal = models.BooleanField(null=False)
    fk_Omc34N1 = models.ForeignKey(OMC34Nivel1, on_delete=models.CASCADE, db_column='fk_Omc34N1', verbose_name='Nivel 2')

    def __str__(self):
        return f'{self.Codigo}: {self.descriSpa}'

    class Meta:
        db_table = "Omc34Nivel2"

class OMC34Nivel3(models.Model):
    idOmc34N3 = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idOmc34N3')
    # cveRol = models.IntegerField(blank=True, null=True)
    Codigo = models.CharField(max_length=9, null=False)
    descriEng = models.CharField(max_length=50, null=False)
    descriSpa = models.CharField(max_length=50, null=False)
    definicionEng = models.CharField(max_length=350, null=False)
    definicionSpa = models.CharField(max_length=330, null=False)
    anioReg = models.IntegerField(null=False)
    regFinal = models.BooleanField(null=False)
    fk_Omc34N2 = models.ForeignKey(OMC34Nivel2, on_delete=models.CASCADE, db_column='fk_Omc34N2', verbose_name='Nivel 2')

    def __str__(self):
        return f'{self.Codigo}: {self.descriSpa}'

    class Meta:
        db_table = "Omc34Nivel3"

class OMC34Nivel4(models.Model):
    idOmc34N4 = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idOmc34N3')
    # cveRol = models.IntegerField(blank=True, null=True)
    Codigo = models.CharField(max_length=11, null=False)
    descriEng = models.CharField(max_length=50, null=False)
    descriSpa = models.CharField(max_length=65, null=False)
    definicionEng = models.CharField(max_length=250, null=False)
    definicionSpa = models.CharField(max_length=300, null=False)
    anioReg = models.IntegerField(null=False)
    regFinal = models.BooleanField(null=False)
    fk_Omc34N3 = models.ForeignKey(OMC34Nivel3, on_delete=models.CASCADE, db_column='fk_Omc34N3', verbose_name='Nivel 3')

    def __str__(self):
        return f'{self.Codigo}: {self.descriSpa}'

    class Meta:
        db_table = "Omc34Nivel4"

