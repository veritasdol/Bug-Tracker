from django.contrib import admin
from .models import Ticket

class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'priority', 'created_by', 'assigned_to', 'created_at', 'updated_at')
    list_filter = ('status', 'priority', 'created_by', 'assigned_to')
    search_fields = ('title', 'description')

admin.site.register(Ticket, TicketAdmin)