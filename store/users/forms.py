from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext, ugettext_lazy as _
from django import forms


User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'password1', 'password2')

class CustomUserChangeForm(UserChangeForm):
    password = None
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')