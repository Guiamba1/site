from django.contrib.auth import forms
from django.db import models

from .models import Usuario

class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = Usuario

class UserCreateForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = Usuario