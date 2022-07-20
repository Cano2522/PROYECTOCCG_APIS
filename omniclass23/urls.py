from rest_framework.routers import DefaultRouter
from omniclass23 import views

router = DefaultRouter()
router.register('OMC23Nivel1', views.OMC23Nivel1, basename = 'OMC23Nivel1')
router.register('OMC23Nivel2', views.OMC23Nivel2, basename = 'OMC23Nivel2')
router.register('OMC23Nivel3', views.OMC23Nivel3, basename = 'OMC23Nivel3')
router.register('OMC23Nivel4', views.OMC23Nivel4, basename = 'OMC23Nivel4')
router.register('OMC23Nivel5', views.OMC23Nivel5, basename = 'OMC23Nivel5')
router.register('OMC23Nivel6', views.OMC23Nivel6, basename = 'OMC23Nivel6')

urlpatterns = router.urls