from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Staff


class StaffAdmin(UserAdmin):
    list_display = ('subject', 'admin_role', 'first_name', 'last_name', 'email')
    search_fields = ('subject', 'admin_role', 'first_name', 'last_name')
    ordering = ('subject',)


admin.site.register(Staff, StaffAdmin)
