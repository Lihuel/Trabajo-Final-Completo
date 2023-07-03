from django.contrib import admin
from . import models

admin.site.site_title = "Noticias"
admin.site.site_header = "La Liga de Fútbol"

admin.site.register(models.Noticias)
class  Noticias(admin.ModelAdmin):
      list_display = ("titulo", "date",)
      search_fields = ("date","titulo",)
      list_filter = ("titulo","date",)
      list_display_links = ("date",)
      ordering = ("date",)
