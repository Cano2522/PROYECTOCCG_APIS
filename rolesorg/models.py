from django.db import models

# Create your models here.
class RolesOrg(models.Model):
    idRolOrg = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idRolOrg')
    cveMo = models.IntegerField(blank=True, null=True)
    Codigo = models.CharField(max_length=11, null=False)
    Consecutivo = models.CharField(max_length=5, null=False)
    descriEng = models.CharField(max_length=65, blank=True, null=True)
    descriSpa = models.CharField(max_length=75, null=False)
    definicionEng = models.CharField(max_length=150, blank=True, null=True)
    definicionSpa = models.CharField(max_length=200, null=False)
    fuenteInf = models.CharField(max_length=45, null=False)
    fecRegInf = models.DateField(null=False)

    def __str__(self):
        return f'{self.Codigo}: {self.descriSpa}'

    class Meta:
        db_table = "RolesOrg"

