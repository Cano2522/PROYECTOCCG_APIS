from rest_framework.routers import DefaultRouter
from unidadesmedida.views import (
    VistaTipoUniMed,
    VistaSubTipUni,
    VistaUnidadesMedida
)

router = DefaultRouter()

router.register('TipoUnidadMedida', VistaTipoUniMed, basename = 'TipoUnidadMedida')
router.register('SubtipoUnidadMedida', VistaSubTipUni, basename = 'SubtipoUnidadMedida')
router.register('UnidadesMedida', VistaUnidadesMedida, basename = 'UnidadesMedida')

urlpatterns = router.urls