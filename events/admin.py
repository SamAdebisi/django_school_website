from django.contrib import admin

from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date',
                    'time_start', 'author')


admin.site.register(Event, EventAdmin)
