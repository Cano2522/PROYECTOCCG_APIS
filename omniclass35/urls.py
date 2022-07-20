from rest_framework.routers import DefaultRouter
from omniclass35 import views

router = DefaultRouter()
router.register('OMC35Nivel1', views.OMC35Nivel1, basename = 'OMC35Nivel1')
router.register('OMC35Nivel2', views.OMC35Nivel2, basename = 'OMC35Nivel2')
router.register('OMC35Nivel3', views.OMC35Nivel3, basename = 'OMC35Nivel3')
router.register('OMC35Nivel4', views.OMC35Nivel4, basename = 'OMC35Nivel4')
router.register('OMC35Nivel5', views.OMC35Nivel5, basename = 'OMC35Nivel5')
router.register('OMC35Nivel6', views.OMC35Nivel6, basename = 'OMC35Nivel6')

urlpatterns = router.urls