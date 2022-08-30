from rest_framework.routers import DefaultRouter
from cementos import views

router = DefaultRouter()

router.register('ListarAcerosRefuerzo', views.ListarAcerosRefuerzo, basename = 'ListarAcerosRefuerzo')
router.register('ListarCementos', views.ListarCementos, basename = 'ListarCementos')

urlpatterns = router.urls