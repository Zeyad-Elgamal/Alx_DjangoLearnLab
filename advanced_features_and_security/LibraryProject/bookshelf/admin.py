from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register Custom User with Django Admin
class CustomUserAdmin(UserAdmin):
    # Define the fields to be displayed in the list view
    list_display = ('username', 'email', 'date_of_birth', 'is_staff', 'is_superuser')
    
    # Define the fields to be used in editing the user model
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('email', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

    # Define the fields to be used when creating a user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'date_of_birth', 'profile_photo', 'password1', 'password2'),
        }),
    )

# Register the custom user and custom admin configuration
admin.site.register(CustomUser, CustomUserAdmin)
