"""principal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from usuarios.views import Login, Logout, UserToken

schema_view = get_schema_view(
   openapi.Info(
      title="Conectar back con front",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="dany.calamateo@gmail.com",),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('apigeograficos/', include('datosgeograficos.urls')),
    path('apiomcroles/', include('omniclass34.urls')),
    path('apiomcproductos/', include('omniclass23.urls')),
    path('apiomcherramienta/', include('omniclass35.urls')),
    path('apiomcmateriales/', include('omniclass41.urls')),
    path('apiproveedores/', include('proveedores.urls')),
    path('apirolesorg/', include('rolesorg.urls')),
    path('apiunidadesmedida/', include('unidadesmedida.urls')),
    path('apiuniformat/', include('uniformat.urls')),
    path('apimateriales/', include('materiales.urls')),
    path('apiusuarios/', include('usuarios.urls')),
    path('apinormativa/', include('normativa.urls')),
    path('login/', Login.as_view(), name = 'Login'),
    path('logout/', Logout.as_view(), name = 'Logout'),
    path('refreshtoken/',UserToken.as_view(), name = 'refresh_token'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
