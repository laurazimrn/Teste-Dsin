from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('registro/', views.cliente_cadastro, name='cliente_cadastro'),
    path('atualizar/', views.cliente_atualizar, name='cliente_atualizar'),
    path('agendamentos/', views.agendamento_lista, name='agendamento_list'),
    path('agendamentos/criar/', views.agendamento_cadastro, name='agendamento_create'),
    path('agendamentos/editar/<int:pk>/', views.agendamento_atualizar, name='agendamento_update'),
    path('agendamentos/excluir/<int:pk>/', views.agendamento_excluir, name='agendamento_delete'),
]