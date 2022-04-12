from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from accounts import forms

# Create your views here.
class SignUpView(CreateView):
    form_class = forms.UserSignUpForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/singup.html'


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('index')


class UserLogoutView(LogoutView):
    template_name = 'accounts/logout.html'
    success_url = reverse_lazy('logout')
