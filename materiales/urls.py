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

urlpatterns = router.urls