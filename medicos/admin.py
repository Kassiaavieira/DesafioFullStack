from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .forms import UserChangeForm, UserCreationForm
from .models import Medico


@admin.register(Medico)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = Medico
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ("Informações Adicionais", {"fields": ()}),
    )