from rest_framework.routers import DefaultRouter
from omniclass34 import views

router = DefaultRouter()
router.register('OMC34Nivel1', views.OMC34Nivel1, basename = 'OMC34Nivel1')
router.register('OMC34Nivel2', views.OMC34Nivel2, basename = 'OMC34Nivel2')
router.register('OMC34Nivel3', views.OMC34Nivel3, basename = 'OMC34Nivel3')
router.register('OMC34Nivel4', views.OMC34Nivel4, basename = 'OMC34Nivel4')

urlpatterns = router.urls