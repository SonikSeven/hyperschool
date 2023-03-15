from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView


class HyperSignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("main_url")
    template_name = "signup.html"


class HyperLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = "login.html"
