
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

from django.views.generic import (
    View,
    FormView,

)

from .forms import (
    LoginForm,
    UserRegisterForm,
)

from .models import User
#


class LoginUser(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_app:panel', args=['inicio'])

    def form_valid(self, form):

        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)

        return super(LoginUser, self).form_valid(form)


class UserRegisterView (FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('home_app:panel', args=['inicio'])

    def form_valid(self, form):

        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['rol'],
            form.cleaned_data['password1'],
            nombre=form.cleaned_data['nombre'],
            apellidos=form.cleaned_data['apellidos'],

        )

        return super(UserRegisterView, self).form_valid(form)


class LogoutView(View):

    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'users_app:user-login'
            )
        )
