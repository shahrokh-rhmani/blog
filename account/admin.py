from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserRegistrationForm
from .models import User


class CustomUserAdmin(UserAdmin):
    add_form = UserRegistrationForm
    # form = CustomUserChangeForm
    model = UserAdmin

admin.site.register(User, CustomUserAdmin)
