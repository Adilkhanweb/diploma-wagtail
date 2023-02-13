from django import forms
from django.utils.translation import gettext_lazy as _

from wagtail.users.forms import UserEditForm, UserCreationForm
from .models import User


class CustomUserEditForm(UserEditForm):
    role = forms.ChoiceField(required=True, label=_("Role"), choices=User.Roles)


class CustomUserCreationForm(UserCreationForm):
    role = forms.ChoiceField(required=True, label=_("Role"), choices=User.Roles.choices, widget=forms.RadioSelect())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
