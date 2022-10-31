from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Cliente, Agendamento


class ClienteCreateView(LoginRequiredMixin ,CreateView):
    
    model = Cliente
    template_name = 'clientes/cadastro.html'
    fields = ['sexo', 'telefone', 'cpf']
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ClienteUpdateView(LoginRequiredMixin, UpdateView):

    model = Cliente
    login_url = reverse_lazy('accounts:login')
    template_name = 'accounts/update_user.html'
    fields = ['sexo', 'telefone', 'cpf']
    success_url = reverse_lazy('accounts:index')

    def get_object(self):
        user = self.request.user
        try:
            return Cliente.objects.get(user=user)
        except Cliente.DoesNotExist:
            return None
        
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        

class AgendamentoCreateView(LoginRequiredMixin, CreateView):

    model = Agendamento
    login_url = 'accounts:login'
    template_name = 'clientes/cadastro.html'
    fields = ['agenda']
    success_url = reverse_lazy('clientes:agendamento_list')
    
    def form_valid(self, form):
        try:
            form.instance.cliente = Cliente.objects.get(user=self.request.user)
            form.save()
        except IntegrityError as e:
            if 'UNIQUE constraint failed' in e.args[0]:
                messages.warning(self.request, 'Você não pode marcar este agendamento')
                return HttpResponseRedirect(reverse_lazy('clientes:agendamento_create'))
        except Cliente.DoesNotExist:
            messages.warning(self.request, 'Complete seu cadastro')
            return HttpResponseRedirect(reverse_lazy('clientes:cliente_cadastro'))
        messages.info(self.request, 'Agendamento marcado com sucesso!')
        return HttpResponseRedirect(reverse_lazy('clientes:agendamento_list'))
    
class AgendamentoUpdateView(LoginRequiredMixin, UpdateView):

    model = Agendamento
    login_url = 'accounts:login'
    template_name = 'clientes/cadastro.html'
    fields = ['agenda']
    success_url = reverse_lazy('profissionais:Agendamento_lista')
    
    def form_valid(self, form):
        form.instance.cliente = Cliente.objects.get(user=self.request.user)
        return super().form_valid(form)
    
class AgendamentoDeleteView(LoginRequiredMixin, DeleteView):
    model = Agendamento
    success_url = reverse_lazy('clientes:agendamento_list')
    template_name = 'form_delete.html'

    def get_success_url(self):
        messages.success(self.request, "Agendamento excluída com sucesso!")
        return reverse_lazy('clientes:agendamento_list')


class AgendamentoListView(LoginRequiredMixin, ListView):
    
    login_url = 'accounts:login'
    template_name = 'clientes/agendamento_list.html'

    def get_queryset(self):
        user=self.request.user
        try:
            cliente = Cliente.objects.get(user=user)
        except Cliente.DoesNotExist:
            messages.warning(self.request, 'Crie um agendamento')
            return None
        try:
            agendamentos = Agendamento.objects.filter(cliente=cliente).order_by('-pk')
        except Agendamento.DoesNotExist:
            messages.warning(self.request, 'Crie um agendamento')
            return None
        return agendamentos


cliente_cadastro = ClienteCreateView.as_view()
cliente_atualizar = ClienteUpdateView.as_view()
agendamento_lista = AgendamentoListView.as_view()
agendamento_cadastro = AgendamentoCreateView.as_view()
agendamento_atualizar = AgendamentoUpdateView.as_view()
agendamento_excluir = AgendamentoDeleteView.as_view()
