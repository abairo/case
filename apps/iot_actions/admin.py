from django.contrib import admin
from .models import IOTAction, IOTEvent


@admin.register(IOTAction)
class IOTActionAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created_at', 'updated_at',)


@admin.register(IOTEvent)
class IOTEventAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'iot_action', 'status', 'value',
                       'user', 'created_at', 'updated_at',)
