from django.contrib import admin
from .models import Pregunta, Opcion

# Register your models here.
@admin.register(Pregunta)
class PreguntaAdmin(admin.ModelAdmin):
   list_display = ('id', 'titulo')
@admin.register(Opcion)
class OpcionAdmin(admin.ModelAdmin):
   pass

