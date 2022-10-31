from django.contrib import admin
from .models import Cliente, Agendamento

    
class ClientAdmin(admin.ModelAdmin):
    list_display = [
        'cpf', 'telefone', 'sexo',
    ]
    
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = [
        'agenda', 'cliente',
    ]
    
    
admin.site.register(Cliente, ClientAdmin)
admin.site.register(Agendamento, AgendamentoAdmin)