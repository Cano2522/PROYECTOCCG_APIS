from distutils.archive_util import make_zipfile
from django.db import models
from materiales.models import Acronimo

# Create your models here.

class Normativa(models.Model):
    idNormativa = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idNormativa')
    nombreSpa = models.CharField(max_length=300,null=True, blank=True)
    nombreEng = models.CharField(max_length=250, null=False)
    fk_Acronimo = models.ForeignKey(Acronimo, on_delete=models.CASCADE, db_column='fk_Acronimo', verbose_name='Acronimo')

    def __str__(self):
        return f'{self.nombreEng}'

    class Meta:
        db_table = 'Normativa'