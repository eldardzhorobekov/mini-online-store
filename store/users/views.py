from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import logout
from users.forms import CustomUserCreationForm, CustomUserChangeForm


User = get_user_model()

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('signin')
    template_name = 'accounts/signup.html'
    

class SignInView(LoginView):
    authentication_form = AuthenticationForm
    template_name = 'accounts/signin.html'

def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('home'))


class ProfileView(LoginRequiredMixin, TemplateView):
    model = User
    template_name = 'accounts/profile.html'


class ProfileEditView(LoginRequiredMixin, UpdateView):
    form_class = CustomUserChangeForm
    template_name = 'accounts/profile_edit.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user
