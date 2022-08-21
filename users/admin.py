from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.models import Group
from .models import User

admin.site.unregister(Group)


class CustomUserAdmin(ModelAdmin):
    fieldsets = (
        (None,
         {'fields': ('first_name', 'last_name', 'email', 'mobile', 'phone', 'password')}),
        ('Permissions', {'fields': ('team', 'is_active')}),
        ('Important Dates', {'fields': ('date_joined', 'last_login')})
    )
    readonly_fields = ('date_joined', 'last_login')
    list_display = ('username', 'first_name', 'last_name', 'email', 'phone', 'mobile', 'team')
    list_filter = ('team', 'is_active')


admin.site.register(User, CustomUserAdmin)
