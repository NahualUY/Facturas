from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.http.response import HttpResponseRedirect
import models
import forms


class Home(TemplateView):
    template_name = 'index.html'


class Clientes(TemplateView):
    template_name = 'clientes.html'

    def get_context_data(self, **kwargs):
        context = super(Clientes, self).get_context_data(**kwargs)

        context['clientes'] = models.Cliente.objects.using(get_db_alias(self.request)).all()

        return context

    def get(self, request, *args, **kwargs):
        if 'accion' in kwargs:
            if kwargs['accion'] == 'eliminar':
                cliente = models.Cliente.objects.using(get_db_alias(self.request)).get(cedula=kwargs['cedula'])
                cliente.delete()
                return HttpResponseRedirect('/clientes')

        return super(Clientes, self).get(request, *args, **kwargs)


class AgregarCliente(FormView):
    form_class = forms.AgregarClienteForm
    template_name = 'agregar_cliente.html'
    success_url = '/clientes'

    def form_valid(self, form):
        cliente = models.Cliente(**form.cleaned_data)
        cliente.save(using=get_db_alias(self.request))
        return super(AgregarCliente, self).form_valid(form)


class Facturas(TemplateView):
    template_name = 'facturas.html'

    def get_context_data(self, **kwargs):
        context = super(Facturas, self).get_context_data(**kwargs)

        context['facturas'] = models.Factura.objects.using(get_db_alias(self.request)).all()

        return context

    def get(self, request, *args, **kwargs):
        if 'accion' in kwargs:
            if kwargs['accion'] == 'eliminar':
                cliente = models.Factura.objects.using(get_db_alias(self.request)).get(numero=kwargs['factura'])
                cliente.delete()
                return HttpResponseRedirect('/facturas')

        return super(Facturas, self).get(request, *args, **kwargs)


class AgregarFactura(FormView):
    form_class = forms.AgregarFacturaForm
    template_name = 'agregar_factura.html'
    success_url = '/facturas'

    def form_valid(self, form):
        factura = models.Factura(**form.cleaned_data)
        factura.save(using=get_db_alias(self.request))
        return super(AgregarFactura, self).form_valid(form)


def get_db_alias(request):
    return request.META['HTTP_HOST'].split('.bd.nahual')[0]
