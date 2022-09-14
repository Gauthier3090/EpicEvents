from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.models import Group
from django.forms import ModelForm
from .models import User

admin.site.unregister(Group)


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'mobile', 'phone', 'password', 'team', 'is_active',
                  'date_joined', 'last_login')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


@admin.register(User)
class CustomUserAdmin(ModelAdmin):
    form = UserForm
    readonly_fields = ('date_joined', 'last_login')
    list_display = ('first_name', 'last_name', 'email', 'phone', 'mobile', 'team')
    list_filter = ('team', 'is_active')
