
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import HttpResponse


from django.views.generic import (
    ListView,
)

from applications.users.models import modulo


class HomePage2(LoginRequiredMixin, ListView):

    context_object_name = 'lista_modulos'
    template_name = 'home/index2.html'

    def get_queryset(self):
        rol = self.request.user.rol_id
        return modulo.objects.modulo_por_rol(rol)

    def get_context_data(self, **kwargs):
        context = super(HomePage2, self).get_context_data(**kwargs)

        context['titulo'] = self.kwargs['marco']
        return context


@xframe_options_exempt
def IndexView(request):
    return HttpResponse("""
   <H2 class="text-center">GLOBAL ENGAGEMENT SOLUTIONS</H2>
<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Rem autem pariatur suscipit commodi
    repellendus praesentium eligendi ullam natus provident quibusdam, omnis, saepe repellat sunt quae.
    Soluta excepturi voluptatum amet iure.</p>""")
