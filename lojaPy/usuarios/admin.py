from django import forms
from django.contrib import admin

from django.contrib.auth import admin as autor
from django.db import models

from .forms import UserCreateForm,UserChangeForm
from .models import Usuario

# Register your models here.

@admin.register(Usuario)
class UserAdmin(autor.UserAdmin):
    form = UserChangeForm
    add_form = UserCreateForm

