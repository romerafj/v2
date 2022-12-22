from .models import lead


def siguiente_lead():
    leads = lead.objects.filter(resultado=1)[:1]
    numero = leads[0].id
    return numero
