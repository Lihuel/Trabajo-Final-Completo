from django.db import models
from datetime import datetime
from django.contrib import admin

admin.site.site_title = "Noticias"
admin.site.site_header = "La Liga de Fútbol"


class Noticias(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.titulo} creada el dia {self.date}" 
    
    class meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'