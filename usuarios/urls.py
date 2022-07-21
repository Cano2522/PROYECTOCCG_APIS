from rest_framework.routers import DefaultRouter
from usuarios import views

router = DefaultRouter()
router.register('Empleados', views.VistaEmpleado, basename = 'Empleados')
router.register('DatosLaborales', views.VistaDatosLaborales, basename = 'DatosLaborales')
router.register('HistorialUsuario', views.VistaHistorialUsuario, basename = 'HistorialUsuario')
router.register('Departamento', views.VistaDepartamento, basename = 'Departamento')
router.register('Cargo', views.VistaCargo, basename = 'Cargo')
router.register('Contrato', views.VistaContrato, basename = 'Contrato')
router.register('Usuario', views.UsuarioViewSet, basename='Usuario')

urlpatterns = router.urls