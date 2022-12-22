
from django.urls import path


from . import views

app_name = "home_app"

urlpatterns = [
   
     
    
    path(
        'panel2/<marco>/',
        views.HomePage2.as_view(),
        name='panel',
    ),
    path(
        'inicio/',
        views.IndexView
    ),
    

]