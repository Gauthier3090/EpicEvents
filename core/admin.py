from django.contrib import admin
from .models import Client, Contract, Event


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Details Client',
         {'fields': ('firstname', 'lastname', 'company_name', 'email', 'phone', 'mobile')}),
        ('Sales', {'fields': ('status', 'sales_contact')}),
        ('Info', {'fields': ('date_created', 'date_updated')})
    )
    readonly_fields = ('date_created', 'date_updated')
    list_display = ('full_name', 'company_name', 'email', 'phone', 'mobile', 'status', 'sales_contact')
    list_filter = ('status', 'sales_contact')
    search_fields = ('firstname', 'lastname', 'company_name', 'sales_contact')

    @staticmethod
    def full_name(obj):
        return f"{obj.lastname}, {obj.firstname}"


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Details Contract', {'fields': ('client', 'amount', 'payment_due')}),
        ('Sales', {'fields': ('status', 'sales_contact')}),
        ('Info', {'fields': ('date_created', 'date_updated')})
    )
    readonly_fields = ('date_created', 'date_updated')
    list_display = ('contract_number', 'sales_contact', 'client', 'amount', 'payment_due', 'status')
    list_filter = ('status', 'sales_contact')
    search_fields = ('contract_number', 'client__lastname')

    @staticmethod
    def contract_number(obj):
        return f"Contract #{obj.id}"


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Details Event',
         {'fields': ('name', 'location', 'contract', 'attendees', 'event_date', 'event_status')}),
        ('Support', {'fields': ('support_contact', 'notes')}),
        ('Info', {'fields': ('date_created', 'date_updated')})
    )
    readonly_fields = ('date_created', 'date_updated')
    list_display = ('name', 'location', 'contract', 'support_contact', 'attendees', 'event_date', 'event_status')
    list_filter = ('event_status', 'support_contact')
    search_fields = ('name', 'location', 'client__lastname')
