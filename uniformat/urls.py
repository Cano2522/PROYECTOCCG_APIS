from rest_framework.routers import DefaultRouter
from uniformat import views

router = DefaultRouter()

router.register('UFTNivel1', views.UFTNivel1, basename = 'UFTNivel1')
router.register('UFTNivel2', views.UFTNivel2, basename = 'UFTNivel2')
router.register('UFTNivel3', views.UFTNivel3, basename = 'UFTNivel3')
router.register('UFTNivel4', views.UFTNivel4, basename = 'UFTNivel4')
router.register('UFTNivel5', views.UFTNivel5, basename = 'UFTNivel5')

urlpatterns = router.urls