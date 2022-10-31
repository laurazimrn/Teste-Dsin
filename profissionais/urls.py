from django.urls import path
from . import views

app_name = 'profissionais'

urlpatterns = [
    path('registro/profissional/', views.profissional_cadastro, name='profissional_cadastro'),
    path('registro/servico/', views.servico_cadastro, name='servico_cadastro'),
    path('agendar/', views.agenda_cadastro, name='agendar_agendamento'),
    path('agendar/atualizar/<int:pk>/', views.agenda_atualizar, name='agendar_agendamento_atualizar'),
    path('agendar/apagar/<int:pk>/', views.agenda_deletar, name='agendar_agendamento_deletar'),
    path('minhas/agendamentos/', views.agenda_lista, name="agenda_lista"),
    path('admim/lista/profissionais/', views.profissional_lista, name="profissionais_lista"),
    path('admim/lista/servicos/', views.servico_lista, name="servico_lista")
    
]