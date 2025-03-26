# accounts/views.py
from django.views.generic import CreateView, FormView, RedirectView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.shortcuts import redirect  # Add this import
from django.contrib.auth import logout  # Add this import
from .forms import UserRegisterForm
from .models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin

class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        # Create or get the Profile instance for the new user
        Profile.objects.get_or_create(user=self.object)
        return response

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

class CustomLogoutView(LogoutView):
    template_name = 'accounts/logout.html'
    success_url = reverse_lazy('accounts:login')

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return redirect(self.success_url)  # Removed the extra quote here

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'