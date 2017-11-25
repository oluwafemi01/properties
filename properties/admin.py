from django.contrib import admin
from .models import properties

class propertiesAdmin(admin.ModelAdmin):
    class Meta:
        model = properties
        
admin.site.register(properties,propertiesAdmin)