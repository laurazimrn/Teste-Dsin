from django.contrib import admin

from profissionais.models import Servico, Profissional, Agenda

class ServicoAdmin(admin.ModelAdmin):
    list_display = ['nome']
    
class ProfissionalAdmin(admin.ModelAdmin):
    list_display = [
        'nome', 'cpf', 'telefone',
    ]
    
class AgendaAdmin(admin.ModelAdmin):
    list_display = [
        'dia', 'profissional', 'horario'
    ]
    
admin.site.register(Servico, ServicoAdmin)
admin.site.register(Profissional, ProfissionalAdmin)
admin.site.register(Agenda, AgendaAdmin)