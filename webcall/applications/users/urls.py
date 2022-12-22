from django.urls import path
from . import views


app_name = 'users_app'


urlpatterns = [
    path(
        '',
        views.LoginUser.as_view(),
        name='user-login',
    ),

    path(
        'register/',
        views.UserRegisterView.as_view(),
        name='user-register',
    ),

    path(
        'logout/',
        views.LogoutView.as_view(),
        name='user-logout',
    ),


]
