from rest_framework.routers import DefaultRouter
from datosgeograficos import views

router = DefaultRouter()
router.register('CodigoPostal', views.VistaCP,basename = 'CodigoPostal')
router.register('Municipio', views.VistaMunDeleg, basename = 'Municipio')
router.register('Estado', views.VistaEstado, basename = 'Estado')
router.register('Pais', views.VistaPais, basename = 'Pais')

urlpatterns = router.urls