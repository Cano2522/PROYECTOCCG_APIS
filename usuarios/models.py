from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from datosgeograficos.models import CP
# Create your models here.

#MODELOS PRINCIPALES PARA EL MANEJO DE USUARIOS
class UserManager(BaseUserManager):
    def _create_user(self, username, correo, nombre, apellidos, genero, rol, password, is_staff, is_superuser, **extra_fields):
        usuario = self.model(
            username = username,
            correo = correo,
            nombre = nombre,
            apellidos = apellidos,
            genero = genero,
            rol = rol,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )

        usuario.set_password(password)
        usuario.save(using=self.db)
        return usuario
    
    def create_user(self, username, correo, nombre, apellidos, genero, rol, password=None, **extra_fields):
        return self._create_user(username, correo, nombre, apellidos, genero, rol, password, False, False, **extra_fields)
    
    def create_superuser(self, username, correo, nombre, apellidos, genero, rol, password=None, **extra_fields):
        return self._create_user(username, correo, nombre, apellidos, genero, rol, password, True, True, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=45, null=False)
    correo = models.EmailField('Correo Electronico', max_length=255, unique=True, null=False)
    nombre = models.CharField('Nombre', max_length=45, blank=True, null=True)
    apellidos = models.CharField('Apellidos', max_length=90, blank=True, null=True)
    genero = models.CharField(max_length=1, blank=True, null=True)
    rol = models.CharField(max_length=15, null=False)
    fechaCreacion = models.DateTimeField(blank=True, null=True,auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['correo', 'nombre', 'apellidos','genero', 'rol']

    def natural_key(self):
        return (self.username)
    
    def __str__(self):
        return f'{self.nombre} {self.apellidos}'

#MODELOS EXTRAS PARA CUBRIR LLAVES FORANEAS DE OTROS MODELOS
class Departamento(models.Model): 
    idDepto = models.BigAutoField(auto_created=True, primary_key= True, serialize= False, verbose_name='idDepto')
    nombre = models.CharField(max_length=45, null=False)  

    def __str__(self):
        return f'{self.nombre}'

    class Meta:
        db_table = 'Departamento'

class Cargo(models.Model): 
    idCargo = models.BigAutoField(auto_created=True, primary_key= True, serialize= False, verbose_name='idCargo')
    nombre = models.CharField(max_length=45, null=False)  
    fk_Depto = models.ForeignKey(Departamento,on_delete=models.CASCADE, db_column='fk_Depto', verbose_name='Departamento')

    def __str__(self):
        return f'{self.nombre}'

    class Meta:
        db_table = 'Cargo'

class Contrato(models.Model): 
    idContrato = models.BigAutoField(auto_created=True, primary_key= True, serialize= False, verbose_name='idContrato')
    tipo = models.CharField(max_length=60, null=False)  

    def __str__(self):
        return f'{self.tipo}'

    class Meta:
        db_table = 'Contrato'


#MODELOS SECUNDARIOS DEL MANEJO DE USUARIOS

class Empleado(models.Model):
    idEmpleado = models.BigAutoField(auto_created=True, primary_key= True, serialize= False, verbose_name='idEmpleado')
    fechaNac = models.DateField(blank=True, null=True)
    lugarNac = models.CharField(max_length=45, blank=True, null=True)
    RFC = models.CharField(max_length=13, blank=True, null=True)  
    CURP = models.CharField(max_length=18, blank=True, null=True)
    celular = models.CharField(max_length=12, blank=True, null=True)
    calle = models.CharField(max_length=45, blank=True, null=True)
    noInt = models.IntegerField(blank=True, null=True)
    noExt = models.IntegerField(blank=True, null=True)
    fk_User = models.ForeignKey(User,on_delete=models.CASCADE, db_column='fk_User', verbose_name='Usuario')
    fk_CP = models.ForeignKey(CP,on_delete=models.CASCADE, blank=True, null=True, db_column='fk_CP', verbose_name='Código Postal')

    def __str__(self):
        return f'{self.CURP}'

    class Meta:
        db_table = 'Empleado'

class DatosLaborales(models.Model):
    idDatosLab = models.BigAutoField(auto_created=True, primary_key= True, serialize= False, verbose_name='idDatosLab')
    codigo = models.CharField(max_length=5,null=False)
    fechaIng = models.DateField(null=False)
    fechaBaja = models.DateField(blank=True,null=True)
    sueldoMensual = models.FloatField(blank=True, null=True)
    referencia1 = models.CharField(max_length=200,blank=True,null=True)
    referencia2 = models.CharField(max_length=200,blank=True,null=True)
    ubicacion = models.CharField(max_length=45,blank=True,null=True)
    procedencia = models.CharField(max_length=10,blank=True,null=True)
    observaciones = models.CharField(max_length=250,blank=True,null=True)
    fk_Empleado = models.ForeignKey(Empleado,on_delete=models.CASCADE, db_column='fk_Empleado', verbose_name='Empleado')
    fk_Cargo = models.ForeignKey(Cargo,on_delete=models.CASCADE, db_column='fk_Cargo', verbose_name='Cargo')
    fk_Contrato = models.ForeignKey(Contrato,on_delete=models.CASCADE, db_column='fk_Contrato', verbose_name='Contrato')

    def __str__(self):
        return f'{self.codigo}'

    class Meta:
        db_table = 'DatosLaborales'

class HistorialUsuario(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key= True, serialize= False, verbose_name='id')
    usuario = models.CharField(max_length=45,null=False)
    entidad = models.CharField(max_length=45,null=False)
    modulo = models.CharField(max_length=45,null=False)
    movimiento = models.CharField(max_length=45,null=False)
    fecha = models.DateTimeField(null=False,auto_now=True)
    observaciones = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.usuario}: {self.movimiento}'

    class Meta:
        db_table = 'HistorialUsuario'