from django.contrib import admin
from .models import *
# Register your models here.
class votacionAdmin(admin.ModelAdmin):
    list_display = ('nombre','estado')
    search_fields = ('nombre','estado')

class votanteAdmin(admin.ModelAdmin):
    list_display = ('nombre','ide','votacion')
    search_fields = ('nombre','ide','votacion')


class candidatoAdmin(admin.ModelAdmin):
    list_display = ('votante','tarjeton')
    search_fields = ('votante','tarjeton')

admin.site.register(votacion, votacionAdmin)
admin.site.register(votante, votanteAdmin)
admin.site.register(candidato, candidatoAdmin)