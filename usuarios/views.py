from datetime import datetime
from django.contrib.sessions.models import Session
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from usuarios.authentication_mixins import Authentication
from usuarios.models import User
from usuarios.serializers import (
    EmpleadoSerializer,
    DatosLaboralesSerializer,
    HistorialUsuarioSerializer,
    CargoSerializer,
    DepartamentoSerializer,
    ContratoSerializer,
    UserTokenSerializer,
    PasswordSerializer,
    EditarUsuarioSerializer,
    UsuarioSerializer,
    ListarUsuarioSerializer,
)
# Create your views here.

#VISTAT PARA EL CONTRO DEL LOGEO Y EL MANEJO DE TOKENS
class UserToken(Authentication, APIView):
    def get(self,request,*args,**kwargs):
        #username = request.GET.get('username')
        try:
            user_token,_ = Token.objects.get_or_create(user = self.user)
            user = UserTokenSerializer(self.user)
            return Response({'token': user_token.key, 'user': user.data})
        except:
            return Response({'error':'Credenciales enviadas incorrectas.'}, status = status.HTTP_400_BAD_REQUEST)

class Login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data=request.data, context = {'request':request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                token,created = Token.objects.get_or_create(user = user)
                user.last_login = datetime.now()
                user.save()
                user_serializer = UserTokenSerializer(user)
                if created:
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'mensaje': 'Inicio de Sesión Exitoso.'
                    }, status = status.HTTP_201_CREATED)
                else:
                    all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                    if all_sessions.exists():
                        for session in all_sessions:
                            session_data = session.get_decoded()
                            if user.id == int(session_data.get('_auth_user_id')):
                                session.delete()
                    token.delete()
                    token = Token.objects.create(user = user)
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Inicio de Sesión Exitoso'
                    }, status = status.HTTP_201_CREATED)
                    # token.delete()
                    # return Response({
                    #     'error': 'Ya se ha iniciado sesión con este usuario.'
                    # }, status = status.HTTP_409_CONFLICT)
            else:
                return Response({'error','Este usuario no puede iniciar sesión'}, status = status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error':'Nombre de usuario o contraseña incorrectos.'}, status = status.HTTP_400_BAD_REQUEST)

class Logout(APIView):
    def post(self, request, *args, **kwargs):
        try:
            # token = request.POST.get('token')
            token = request.data['token']
            #print(token)
            token = Token.objects.filter(key = token).first()
            if token:
                user = token.user

                all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete()
                token.delete()

                session_message = 'Sesiones de usuario eliminadas.'
                token_message = 'Token eliminado.'
                return Response({'mensaje_token':token_message, 'mensaje_sesion':session_message}, status = status.HTTP_200_OK)
            return Response({'error': 'No se ha encontrado un usuario con estas credenciales'}, status = status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error':'No se han encontrado token en la petición'}, status = status.HTTP_409_CONFLICT)

class UsuarioViewSet(Authentication,viewsets.GenericViewSet):
    model = User
    serializer_class = UsuarioSerializer
    list_serializer_class = ListarUsuarioSerializer
    query = None

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.model.objects.all().values('id','username','Correo','password','Nombre','Apellidos','Genero','Rol','fechaCreacion','last_login')
        return self.queryset
    
    @action(detail=True, methods=['post'])
    def set_password(self, request, pk=None):
        user = self.get_object(pk)
        password_serializer = PasswordSerializer(data=request.data)
        if password_serializer.is_valid():
            user.set_password(password_serializer.validated_data['password'])
            user.save()
            return Response({'mensaje': 'Contraseña actualizada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error':password_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['get'])
    def set_active_on(self, request, pk=None):
        user = self.get_object(pk)
        if user.is_active == False:
            user.is_active = True
            user.save()
            return Response({'mensaje': 'Usuario activado correctamente'}, status = status.HTTP_200_OK)
        else:
            return Response({'mensaje': 'El usuario ya esta activo'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'])
    def set_active_off(self, request, pk=None):
        user = self.get_object(pk)
        if user.is_active == True:
            user.is_active = False
            user.save()
            return Response({'mensaje': 'Usuario desactivado correctamente'}, status = status.HTTP_200_OK)
        else:
            return Response({'mensaje': 'El usuario ya esta desactivado'}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        usuarios = self.get_queryset()
        users_serializer = self.list_serializer_class(usuarios, many=True)
        return Response(users_serializer.data, status = status.HTTP_200_OK)

    def create(self, request):
        user_serializer = self.serializer_class(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status = status.HTTP_201_CREATED)
        return Response({'error':user_serializer.errors}, status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        user = self.get_object(pk)
        user_serializer = self.serializer_class(user)
        return Response(user_serializer.data)
    
    def update(self, request, pk=None):
        usuario = self.get_object(pk)
        user_serializer = EditarUsuarioSerializer(usuario, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status = status.HTTP_200_OK)
        return Response({'error':user_serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        usuario = User.objects.filter(id=pk).first()
        # usuario = self.model.objects.filter(id=pk).update(is_active=False)
        if usuario:
            usuario.delete()
            return Response({'mensaje':'Usuario eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'mensaje':'No se a encontrado un usuario con estos datos'}, status = status.HTTP_404_NOT_FOUND)

#VISTAS PARA EL CONTROL DE LAS TABLAS SECUNDARIAS DE USUARIOS

class VistaEmpleado(Authentication,viewsets.ModelViewSet):
    serializer_class = EmpleadoSerializer
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idEmpleado = pk).first()

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response({'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe un Registro con esos datos'}, status = status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk=None):
        registro = self.get_queryset().filter(idEmpleado=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un Registro con estos datos!'}, status = status.HTTP_404_NOT_FOUND)

class VistaDatosLaborales(Authentication,viewsets.ModelViewSet):
    serializer_class = DatosLaboralesSerializer
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idDatosLab = pk).first()

    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response({'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe un Registro con esos datos'}, status = status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk=None):
        registro = self.get_queryset().filter(idDatosLab=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un Registro con estos datos!'}, status = status.HTTP_404_NOT_FOUND)

class VistaHistorialUsuario(Authentication,viewsets.ModelViewSet):
    serializer_class = HistorialUsuarioSerializer
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(id = pk).first()
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response({'error':serializer.errors}, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'No existe un Registro con esos datos'}, status = status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        registro = self.get_queryset().filter(id=pk).first()
        if registro:
            registro.delete()
            return Response({'mensaje':'Registro eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un Registro con estos datos!'}, status = status.HTTP_404_NOT_FOUND)

#VISTAS PARA EL CONTROL DE LAS TABLAS EXTRAS DE USUARIOS
class VistaCargo(Authentication,viewsets.ModelViewSet):
    serializer_class = CargoSerializer
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idCargo = pk).first()

class VistaDepartamento(Authentication,viewsets.ModelViewSet):
    serializer_class = DepartamentoSerializer
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idDepto = pk).first()

class VistaContrato(Authentication,viewsets.ModelViewSet):
    serializer_class = ContratoSerializer
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(idContrato = pk).first()
