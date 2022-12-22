from django.urls import reverse_lazy
from . import funciones
from django.http import HttpResponse
from . import funciones
from django.views.generic import (
    UpdateView,
    ListView,
    View
)
from .models import lead


class LeadsUpdateView(UpdateView):

    model = lead
    template_name = "llamadas/Update.html"
    fields = [
        'telefono',
        'nombre',
        'apellidos',
        'direccion',
        'poblacion',
        'observaciones',
        'resultado',
    ]
    leads = lead.objects.filter(resultado=1)[:1]
    numero = leads[0].id

    def get_success_url(self):
        leads = lead.objects.filter(resultado=1)[:1]
        numero = leads[0].id
        print('El numero siguiente es ' + str(numero))
        # direccion= '../' + str(numero)
        return (reverse_lazy('llamadas_app:modificar_lead', kwargs={'pk': numero}))
        # HttpResponseRedirect(reverse_lazy('llamadas_app:modificar_lead', kwargs={'pk':2}))

    success_url = '/home'
    # success_url = direccion


class ListaLeadsListView(ListView):
    model = lead
    template_name = "llamadas/leads.html"
    context_object_name = 'leads'


class ListaLeadsPdf(View):
    def get(self, request, *args, **kwargs):
        leads = lead.objects.all()
        data = {
            'leads': leads
        }
        pdf = funciones.render_to_pdf('llamadas/leadspdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
