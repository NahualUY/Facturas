from django.conf.urls import patterns, include, url
from django.contrib import admin
import views

urlpatterns = patterns('',
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^clientes$', views.Clientes.as_view(), name='clientes'),
    url(r'^clientes/agregar$', views.AgregarCliente.as_view(), name='agregar-cliente'),
    url(r'^clientes/eliminar/(?P<cedula>.*)$', views.Clientes.as_view(), name='eliminar-clientes', kwargs={'accion': 'eliminar'}),
    url(r'^facturas$', views.Facturas.as_view(), name='facturas'),
    url(r'^facturas/agregar$', views.AgregarFactura.as_view(), name='agregar-factura'),
    url(r'^facturas/eliminar/(?P<factura>\d+)$', views.Facturas.as_view(), name='eliminar-facturas', kwargs={'accion': 'eliminar'}),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
