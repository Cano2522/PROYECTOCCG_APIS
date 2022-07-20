from rest_framework.routers import DefaultRouter
from proveedores import views

router = DefaultRouter()
router.register('Proveedor', views.VistaProveedor, basename = 'Proveedor')
router.register('Marca', views.VistaMarca, basename = 'Marca')
router.register('SectorMercado', views.VistaSectorMercado, basename = 'SectorMercado')
router.register('ProveedorMarca', views.VistaProveedorMarca, basename = 'ProveedorMarca')
router.register('SucursalProveedor', views.VistaSucursalProv, basename = 'SucursalProveedor')
router.register('SectorProveedor', views.VistaSectorProv, basename = 'SectorProveedor')
router.register('ListarSectorXProveedor', views.ListarSectorXProveedor, basename = 'ListarSectorXProveedor')
router.register('ListarMarcaXProveedor', views.ListarMarcaXProveedor, basename = 'ListarMarcaXProveedor')
router.register('ListarSucursalXProveedor', views.ListarSucursalXProveedor, basename = 'ListarSucursalXProveedor')

urlpatterns = router.urls