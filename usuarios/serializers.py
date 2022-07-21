from rest_framework import serializers
from usuarios.models import (
    Empleado,
    DatosLaborales,
    HistorialUsuario,
    Departamento,
    Cargo,
    Contrato,
    User
)

#SERIALIZERS PARA EL MANEJO DE LOS USUARIOS
class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','Correo','Nombre','Apellidos', 'Rol']

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password','Correo','Nombre','Apellidos','Genero','Rol','fechaCreacion']

    def create(self,validated_data):
        usuario = User(**validated_data)
        usuario.set_password(validated_data['password']) #this encrypts the password 
        usuario.save()
        return usuario

    def update(self,instance,validated_data):
        usuario_actualizado = super().update(instance,validated_data) #this encrypts the password 
        usuario_actualizado.set_password(validated_data['password'])
        usuario_actualizado.save()
        return usuario_actualizado

class EditarUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','Correo','Nombre','Apellidos','Genero','Rol']

class ListarUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

    def to_representation(self,instance):
        return {
            'id': instance['id'],
            'username': instance['username'],
            'Correo': instance['Correo'],
            'password': instance['password'],
            'Nombre': instance['Nombre'],
            'Apellidos': instance['Apellidos'],
            'Genero': instance['Genero'],
            'Rol': instance['Rol'],
            'fechaCreacion': instance['fechaCreacion'],
            'last_login': instance['last_login']
        }

class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128, min_length=6, write_only=True)
    password2 = serializers.CharField(max_length=128, min_length=6, write_only=True)

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {'password':'Debe ingresar ambas contraseñas iguales'}
            )
        return data

# SERIALIZERS PARA MANEJAR TABLAS SECUNDARIOAS DE USUARIOS
class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ['idEmpleado','fechaNac','lugarNac','RFC','CURP','Cel','Calle','noInt','noExt','fk_User','fk_CP']

class DatosLaboralesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosLaborales
        fields = ['idDatosLab','Codigo','fechaIng','fechaBaja','sueldoMensual','Referencia1','Referencia2','Ubicacion','Procedencia','Observaciones','fk_Empleado','fk_Cargo','fk_Contrato']

class HistorialUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialUsuario
        fields = ['id','usuario','entidad','modulo','movimiento','fecha','observaciones']

# SERIALIZERS PARA MANEJAR TABLAS EXTRAS DE USUARIOS
class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ['idDepto','Nombre']

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = ['idCargo','Nombre','fk_Depto']

class ContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contrato
        fields = ['idContrato','Tipo']