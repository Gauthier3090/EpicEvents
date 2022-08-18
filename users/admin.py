from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import Group
from django.contrib.auth.models import User

admin.site.unregister(Group)


class UserAdminCustom(UserAdmin):
    fieldsets = (
        ('Infos User', {'fields': ('username', 'password', 'firstname', 'lastname', 'email', 'phone', 'mobile')}),
        ('Permissions', {'fields': ('team',)}),
        ('Historic', {'fields': ('date_joined', 'last_login')})
    )
    readonly_fields = ('date_joined', 'last_login')
    list_display = ('username', 'firstname', 'lastname', 'email', 'phone', 'mobile', 'team')
    list_filter = ('team', 'is_active')


admin.site.register(User, UserAdminCustom)
