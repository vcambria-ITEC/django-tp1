from django.contrib import admin
from .models import Clima, Ciudad

admin.site.register(Clima)

@admin.register(Ciudad)
class CiudadAdmin(admin.ModelAdmin):
    list_display = ("nombre_ciudad",)
    search_fields = ("nombre_ciudad",)
