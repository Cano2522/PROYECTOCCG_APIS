from rest_framework.routers import DefaultRouter
from normativa import views

router = DefaultRouter()

router.register('Normativa', views.VistaNormativa, basename='Normativa')
router.register('ListarNormativaAcronimo', views.ListarNormativaAcronimo, basename='ListarNormativaAcronimo')

urlpatterns = router.urls
