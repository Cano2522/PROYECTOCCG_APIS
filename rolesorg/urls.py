from rest_framework.routers import DefaultRouter
from rolesorg import views

router = DefaultRouter()

router.register('RolesOrg', views.RolesOrg, basename = 'RolesOrg')
router.register('ListarRolesXOMC23N2', views.ListarRolesXOMC23N2, basename = 'ListarRolesXOMC23N2')
router.register('ListarRolesXOMC23N3', views.ListarRolesXOMC23N3, basename = 'ListarRolesXOMC23N3')
router.register('ListarRolesXOMC23N4', views.ListarRolesXOMC23N4, basename = 'ListarRolesXOMC23N4')

urlpatterns = router.urls