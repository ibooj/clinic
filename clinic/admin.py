from django.contrib import admin

from .models import Doctor, Registry


class RegistryAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'doctor', 'date', 'time')
    list_filter = ['doctor']


admin.site.register(Registry, RegistryAdmin)
admin.site.register(Doctor)
