from django.urls import path


from . import views

app_name = "llamadas_app"

urlpatterns = [

    path(
        'update-lead/<pk>/',
        views.LeadsUpdateView.as_view(),
        name='modificar_lead'
    ),
    path(
        'listaleads',
        views.ListaLeadsListView.as_view(),
        name='listaLeads'
    ),
    path(
        'listaleadspdf',
        views.ListaLeadsPdf.as_view(),
        name='leads_all'
    )
]
