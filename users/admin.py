from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.models import Group
from .models import User

admin.site.unregister(Group)


@admin.register(User)
class CustomUserAdmin(ModelAdmin):
    fieldsets = (
        ("Personal Info",
         {'fields': ('username', 'first_name', 'last_name', 'email', 'mobile', 'phone', 'password')}),
        ('Permissions', {'fields': ('team', 'is_active')}),
        ('Important Dates', {'fields': ('date_joined', 'last_login')})
    )
    readonly_fields = ('date_joined', 'last_login')
    list_display = ('first_name', 'last_name', 'email', 'phone', 'mobile', 'team')
    list_filter = ('team', 'is_active')
