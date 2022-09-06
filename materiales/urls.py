from posixpath import basename
from rest_framework.routers import DefaultRouter
from materiales import views

router = DefaultRouter()

router.register('Material', views.VistaMaterial, basename = 'Materiales')
router.register('Concreto', views.VistaConcreto, basename = 'Concreto')
router.register('CaracEspe', views.VistaCaracEspe, basename = 'CaracEspe')
router.register('ListarEsfuerzo', views.VistaEsfuerzo, basename = 'ListarEsfuerzo')
router.register('ListarValorEsfuerzo', views.VistaValorEsfuerzo, basename = 'ListarValorEsfuerzo')
router.register('ListarTipoResistencia', views.VistaTipoResistencia, basename = 'ListarTipoResistencia')
router.register('ListarAplPrincipales', views.VistaAplPrincipales, basename = 'ListarAplPrincipales')
router.register('ListarTMA', views.VistaTMA, basename = 'ListarTMA')
router.register('ListarRevenimiento', views.VistaRevenimiento, basename = 'ListarRevenimiento')
router.register('ListarDensidad', views.VistaDensidad, basename = 'ListarDensidad')
router.register('ListarSistColocacion', views.VistaSistColocacion, basename = 'ListarSistColocacion')
router.register('ListarClasExposicion', views.VistaClasExposicion, basename = 'ListarClasExposicion')
router.register('ListarFlujoRev', views.VistaFlujoRev, basename = 'ListarFlujoRev')
router.register('ListarIonCloruro', views.VistaIonCloruro, basename = 'ListarIonCloruro')
router.register('ListarFibraConcre', views.VistaFibraConcre, basename = 'ListarFibraConcre')
router.register('ListarConcretosMateriales', views.ListarConcretosMateriales, basename = 'ListarConcretosMateriales')
router.register('ListarMaterialContratista', views.ListarMaterialContratista, basename = 'ListarMaterialContratista')
# FUNCIONES CORRESPONDIENTES A CEMENTOS
router.register('Cemento', views.VistaCemento, basename = 'Cemento')
router.register('ListarClaseResist', views.VistaClaseResist, basename = 'ListarClaseResist')
router.register('ListarClasifCemento', views.VistaClasifCemento, basename = 'ListarClasifCemento')
router.register('ListarCementos', views.ListarCementos, basename = 'ListarCementos')
# FUNCIONES CORRESPONDIENTES A ACERO REFORZADO
router.register('AceroRefuerzo', views.VistaAceroRefuerzo, basename = 'AceroRefuerzo')
router.register('Dimensiones', views.VistaDimensiones, basename = 'Dimensiones')
router.register('ListarGrado', views.VistaGrado, basename = 'ListarGrado')
router.register('ListarAcerosRefuerzo', views.ListarAcerosRefuerzo, basename = 'ListarAcerosRefuerzo')

urlpatterns = router.urls