from django.db import models

# Create your models here.
class OMC35Nivel1(models.Model):
    idOmc35N1 = models.BigAutoField(auto_created=True, primary_key= True, serialize= False, verbose_name='idOmc35N1')
    codigo = models.CharField(max_length=9, null=False)
    descriEng = models.CharField(max_length=30, null= False)
    descriSpa = models.CharField(max_length=100, null= False)
    definicionEng = models.CharField(max_length=150, blank=True, null= True)
    definicionSpa = models.CharField(max_length=150, blank=True, null= True)
    anioReg = models.IntegerField(null=False)
    fk_EnvOMC = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.codigo}: {self.descriSpa}'

    class Meta:
        db_table = "Omc35Nivel1"

class OMC35Nivel2(models.Model):
    idOmc35N2 = models.BigAutoField(auto_created=True, primary_key= True, serialize= False, verbose_name='idOmc35N1')
    codigo = models.CharField(max_length=9, null=False)
    descriEng = models.CharField(max_length=50, null= False)
    descriSpa = models.CharField(max_length=80, null= False)
    definicionEng = models.CharField(max_length=150, blank=True, null= True)
    definicionSpa = models.CharField(max_length=150, blank=True, null= True)
    anioReg = models.IntegerField(null=False)
    fk_Omc35N1 = models.ForeignKey(OMC35Nivel1,on_delete=models.CASCADE, db_column='fk_Omc35N1', verbose_name='Nivel 1')

    def __str__(self):
        return f'{self.codigo}: {self.descriSpa}'

    class Meta:
        db_table = "Omc35Nivel2"

class OMC35Nivel3(models.Model):
    idOmc35N3 = models.BigAutoField(auto_created=True, primary_key= True, serialize= False, verbose_name='idOmc35N3')
    cveHe = models.IntegerField(blank=True,null=True)
    codigo = models.CharField(max_length=9, null=False)
    descriEng = models.CharField(max_length=60, null= False)
    descriSpa = models.CharField(max_length=80, null= False)
    definicionEng = models.CharField(max_length=150, blank=True, null= True)
    definicionSpa = models.CharField(max_length=150, blank=True, null= True)
    anioReg = models.IntegerField(null=False)
    regFinal = models.BooleanField(null=False)
    fk_Omc35N2 = models.ForeignKey(OMC35Nivel2,on_delete=models.CASCADE, db_column='fk_Omc35N2', verbose_name='Nivel 2')

    def __str__(self):
        return f'{self.codigo}: {self.descriSpa}'

    class Meta:
        db_table = "Omc35Nivel3"

class OMC35Nivel4(models.Model):
    idOmc35N4 = models.BigAutoField(auto_created=True, primary_key= True, serialize= False, verbose_name='idOmc35N4')
    cveHe = models.IntegerField(blank=True,null=True)
    codigo = models.CharField(max_length=11, null=False)
    descriEng = models.CharField(max_length=80, null= False)
    descriSpa = models.CharField(max_length=90, null= False)
    definicionEng = models.CharField(max_length=150, blank=True, null= True)
    definicionSpa = models.CharField(max_length=150, blank=True, null= True)
    anioReg = models.IntegerField(null=False)
    regFinal = models.BooleanField(null=False)
    fk_Omc35N3 = models.ForeignKey(OMC35Nivel3,on_delete=models.CASCADE, db_column='fk_Omc35N3', verbose_name='Nivel 3')

    def __str__(self):
        return f'{self.codigo}: {self.descriSpa}'

    class Meta:
        db_table = "Omc35Nivel4"

class OMC35Nivel5(models.Model):
    idOmc35N5 = models.BigAutoField(auto_created=True, primary_key= True, serialize= False, verbose_name='idOmc35N5')
    cveHe = models.IntegerField(blank=True,null=True)
    codigo = models.CharField(max_length=13, null=False)
    descriEng = models.CharField(max_length=90, null= False)
    descriSpa = models.CharField(max_length=100, null= False)
    definicionEng = models.CharField(max_length=150, blank=True, null= True)
    definicionSpa = models.CharField(max_length=150, blank=True, null= True)
    anioReg = models.IntegerField(null=False)
    regFinal = models.BooleanField(null=False)
    fk_Omc35N4 = models.ForeignKey(OMC35Nivel4,on_delete=models.CASCADE, db_column='fk_Omc35N4', verbose_name='Nivel 4')

    def __str__(self):
        return f'{self.codigo}: {self.descriSpa}'

    class Meta:
        db_table = "Omc35Nivel5"

class OMC35Nivel6(models.Model):
    idOmc35N6 = models.BigAutoField(auto_created=True, primary_key= True, serialize= False, verbose_name='idOmc35N6')
    cveHe = models.IntegerField(blank=True,null=True)
    codigo = models.CharField(max_length=15, null=False)
    descriEng = models.CharField(max_length=75, null= False)
    descriSpa = models.CharField(max_length=100, null= False)
    definicionEng = models.CharField(max_length=150, blank=True, null= True)
    definicionSpa = models.CharField(max_length=150, blank=True, null= True)
    anioReg = models.IntegerField(null=False)
    regFinal = models.BooleanField(null=False)
    fk_Omc35N5 = models.ForeignKey(OMC35Nivel5,on_delete=models.CASCADE, db_column='fk_Omc35N5', verbose_name='Nivel 5')

    def __str__(self):
        return f'{self.codigo}: {self.descriSpa}'

    class Meta:
        db_table = "Omc35Nivel6"
    