from rest_framework.routers import DefaultRouter
from omniclass41 import views

router = DefaultRouter()
router.register('OMC41Nivel1', views.OMC41Nivel1, basename = 'OMC41Nivel1')
router.register('OMC41Nivel2', views.OMC41Nivel2, basename = 'OMC41Nivel2')
router.register('OMC41Nivel3', views.OMC41Nivel3, basename = 'OMC41Nivel3')
router.register('OMC41Nivel4', views.OMC41Nivel4, basename = 'OMC41Nivel4')
router.register('OMC41Nivel5', views.OMC41Nivel5, basename = 'OMC41Nivel5')
router.register('OMC41Nivel6', views.OMC41Nivel6, basename = 'OMC41Nivel6')

urlpatterns = router.urls