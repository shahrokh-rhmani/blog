from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserRegistrationForm
from .models import User


class CustomUserAdmin(UserAdmin):
    add_form = UserRegistrationForm
    list_display = UserAdmin.list_display + ('is_author', 'special_user',)
    # fieldsets = UserAdmin.fieldsets
    # fieldsets = ['is_author']
    # form = CustomUserChangeForm
    model = UserAdmin

UserAdmin.fieldsets[2][1]['fields'] = (
    'is_active',
    'is_staff',
    'is_superuser',
    'is_author',
    'special_user',
    'groups',
    'user_permissions',

)


admin.site.register(User, CustomUserAdmin)
