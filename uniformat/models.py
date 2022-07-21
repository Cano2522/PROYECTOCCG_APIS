from django.db import models

# Create your models here.

class UFTCategorias(models.Model):
    idUftCat = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idUftCat')  #asi se resuelve el problema del error del id
    Codigo = models.CharField(max_length=1)
    descriEng = models.CharField(max_length=45)
    descriSpa = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f'Categoria {self.Codigo}: {self.descriSpa}'

    class Meta:
        db_table = "UftCategorias" #con esto se arregla el detalle del nombre de la tabla
    

class UFTNivel2(models.Model):
    idUftN2 = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idUftN2')  #asi se resuelve el problema del error del id
    Codigo = models.CharField(max_length=3)
    descriEng = models.CharField(max_length=70)
    descriSpa = models.CharField(max_length=70, null=True, blank=True)
    explicacionEng = models.CharField(max_length=70, null=True, blank=True)
    explicacionSpa = models.CharField(max_length=100, null=True, blank=True)
    fk_UftCat = models.ForeignKey(UFTCategorias, on_delete=models.CASCADE, db_column='fk_UftCat', verbose_name='Categoria') # con db_column se agrega el error del id

    def __str__(self):
        return f'Nivel 2: {self.descriSpa}'

    class Meta:
        db_table = "UFTNivel2" #con esto se arregla el detalle del nombre de la tabla

class UFTNivel3(models.Model):
    idUftN3 = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idUftN3')  #asi se resuelve el problema del error del id
    Codigo = models.CharField(max_length=10)
    descriEng = models.CharField(max_length=150)
    descriSpa = models.CharField(max_length=150, null=True, blank=True)
    explicacionEng = models.CharField(max_length=700, null=True, blank=True)
    explicacionSpa = models.CharField(max_length=800, null=True, blank=True)
    Observaciones = models.CharField(max_length=100, null=True, blank=True)
    fk_UftN2 = models.ForeignKey(UFTNivel2, on_delete=models.CASCADE, db_column='fk_UftN2', verbose_name='Categoria Nivel 2') # con db_column se agrega el error del id

    def __str__(self):
        return f'Nivel 3: {self.descriSpa}'

    class Meta:
        db_table = "UFTNivel3" #con esto se arregla el detalle del nombre de la tabla

class UFTNivel4(models.Model):
    idUftN4 = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idUftN4')  #asi se resuelve el problema del error del id
    Codigo = models.CharField(max_length=10)
    descriEng = models.CharField(max_length=200)
    descriSpa = models.CharField(max_length=200, null=True, blank=True)
    explicacionEng = models.TextField(blank=True, null=True)
    explicacionSpa = models.TextField(blank=True, null=True)
    Observaciones = models.CharField(max_length=100, null=True, blank=True)
    fk_UftN3 = models.ForeignKey(UFTNivel3, on_delete=models.CASCADE, db_column='fk_UftN3', verbose_name='Categoria Nivel 3') # con db_column se agrega el error del id

    def __str__(self):
        return f'Nivel 4: {self.descriSpa}'

    class Meta:
        db_table = "UFTNivel4" #con esto se arregla el detalle del nombre de la tabla

class UFTNivel5(models.Model):
    idUftN5 = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idUftN5')  #asi se resuelve el problema del error del id
    Codigo = models.CharField(max_length=10)
    descriEng = models.CharField(max_length=100)
    descriSpa = models.CharField(max_length=150, null=True, blank=True)
    explicacionEng = models.CharField(max_length=200, null=True, blank=True)
    explicacionSpa = models.CharField(max_length=250, null=True, blank=True)
    Observaciones = models.CharField(max_length=100, null=True, blank=True)
    fk_UftN4 = models.ForeignKey(UFTNivel4, on_delete=models.CASCADE, db_column='fk_UftN4', verbose_name='Categoria Nivel 4') # con db_column se agrega el error del id

    def __str__(self):
        return f'Nivel 5: {self.descriSpa}'

    class Meta:
        db_table = "UFTNivel5" #con esto se arregla el detalle del nombre de la tabla