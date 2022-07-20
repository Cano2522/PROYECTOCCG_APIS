from django.db import models

# Create your models here.
class OMC41Nivel1(models.Model):
    idOmc41N1 = models.BigAutoField(auto_created=True, primary_key= True, serialize= False, verbose_name='idOmc41N1')
    Codigo = models.CharField(max_length=9, null=False)
    descriEng = models.CharField(max_length=25, null= False)
    descriSpa = models.CharField(max_length=25, blank= True, null= True)
    definicionEng = models.CharField(max_length=150, null= False)
    definicionSpa = models.CharField(max_length=150, null= False)
    anioReg = models.IntegerField(null=False)

    def __str__(self):
        return f'{self.Codigo}: {self.descriSpa}'

    class Meta:
        db_table = "Omc41Nivel1"

class OMC41Nivel2(models.Model):
    idOmc41N2 = models.BigAutoField(auto_created=True, primary_key= True, serialize= False, verbose_name='idOmc41N2')
    Codigo = models.CharField(max_length=9, null=False)
    descriEng = models.CharField(max_length=35, null= False)
    descriSpa = models.CharField(max_length=35, null= False)
    definicionEng = models.CharField(max_length=150, null= False)
    definicionSpa = models.CharField(max_length=250, null= False)
    anioReg = models.IntegerField(null=False)
    fk_Omc41N1 = models.ForeignKey(OMC41Nivel1, on_delete=models.CASCADE, db_column='fk_Omc41N1', verbose_name='Nivel 1')

    def __str__(self):
        return f'{self.Codigo}: {self.descriSpa}'

    class Meta:
        db_table = "Omc41Nivel2"

class OMC41Nivel3(models.Model):
    idOmc41N3 = models.BigAutoField(auto_created=True, primary_key= True, serialize= False, verbose_name='idOmc41N3')
    numMat = models.IntegerField(blank=True, null=True)
    Codigo = models.CharField(max_length=9, null=False)
    descriEng = models.CharField(max_length=40, null= False)
    descriSpa = models.CharField(max_length=45, null= False)
    definicionEng = models.CharField(max_length=270, null= False)
    definicionSpa = models.CharField(max_length=300, null= False)
    anioReg = models.IntegerField(null=False)
    regFinal = models.BooleanField(null=False)
    fk_Omc41N2 = models.ForeignKey(OMC41Nivel2, on_delete=models.CASCADE, db_column='fk_Omc41N2', verbose_name='Nivel 2')

    def __str__(self):
        return f'{self.Codigo}: {self.descriSpa}'

    class Meta:
        db_table = "Omc41Nivel3"

class OMC41Nivel4(models.Model):
    idOmc41N4 = models.BigAutoField(auto_created=True, primary_key= True, serialize= False, verbose_name='idOmc41N4')
    numMat = models.IntegerField(blank=True, null=True)
    Codigo = models.CharField(max_length=11, null=False)
    descriEng = models.CharField(max_length=50, null= False)
    descriSpa = models.CharField(max_length=55, null= False)
    definicionEng = models.CharField(max_length=350, null= False)
    definicionSpa = models.CharField(max_length=400, null= False)
    anioReg = models.IntegerField(null=False)
    regFinal = models.BooleanField(null=False)
    fk_Omc41N3 = models.ForeignKey(OMC41Nivel3, on_delete=models.CASCADE, db_column='fk_Omc41N3', verbose_name='Nivel 3')

    def __str__(self):
        return f'{self.Codigo}: {self.descriSpa}'

    class Meta:
        db_table = "Omc41Nivel4"

class OMC41Nivel5(models.Model):
    idOmc41N5 = models.BigAutoField(auto_created=True, primary_key= True, serialize= False, verbose_name='idOmc41N5')
    numMat = models.IntegerField(blank=True, null=True)
    Codigo = models.CharField(max_length=13, null=False)
    descriEng = models.CharField(max_length=35, null= False)
    descriSpa = models.CharField(max_length=45, null= False)
    definicionEng = models.CharField(max_length=350, null= False)
    definicionSpa = models.CharField(max_length=400, null= False)
    anioReg = models.IntegerField(null=False)
    regFinal = models.BooleanField(null=False)
    fk_Omc41N4 = models.ForeignKey(OMC41Nivel4, on_delete=models.CASCADE, db_column='fk_Omc41N4', verbose_name='Nivel 4')

    def __str__(self):
        return f'{self.Codigo}: {self.descriSpa}'

    class Meta:
        db_table = "Omc41Nivel5"

class OMC41Nivel6(models.Model):
    idOmc41N6 = models.BigAutoField(auto_created=True, primary_key= True, serialize= False, verbose_name='idOmc41N6')
    numMat = models.IntegerField(blank=True, null=True)
    Codigo = models.CharField(max_length=15, null=False)
    descriEng = models.CharField(max_length=30, null= False)
    descriSpa = models.CharField(max_length=30, null= False)
    definicionEng = models.CharField(max_length=250, null= False)
    definicionSpa = models.CharField(max_length=300, null= False)
    anioReg = models.IntegerField(null=False)
    regFinal = models.BooleanField(null=False)
    fk_Omc41N5 = models.ForeignKey(OMC41Nivel5, on_delete=models.CASCADE, db_column='fk_Omc41N5', verbose_name='Nivel 5')

    def __str__(self):
        return f'{self.Codigo}: {self.descriSpa}'

    class Meta:
        db_table = "Omc41Nivel6"