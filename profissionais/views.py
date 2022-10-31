from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Profissional, Agenda, Servico


class TestMixinIsAdmin(UserPassesTestMixin):
    def test_func(self):
        is_admin_or_is_staff = self.request.user.is_superuser or \
            self.request.user.is_staff
        return bool(is_admin_or_is_staff)

    def handle_no_permission(self):
        messages.error(
            self.request, "Você não tem permissões!"
        )
        return redirect("accounts:index")

class ProfissionalCreateView(LoginRequiredMixin, TestMixinIsAdmin, CreateView):

    model = Profissional
    login_url = 'accounts:login'
    template_name = 'profissionais/cadastro.html'
    fields = ['nome', 'cpf', 'email', 'telefone', 'servico']
    success_url = reverse_lazy('profissionais:profissionais_lista')
    
class ProfissionalListView(LoginRequiredMixin, TestMixinIsAdmin, ListView):
    
    login_url = 'accounts:login'
    template_name = 'profissionais/profissionais_list.html'

    def get_queryset(self):
        return Profissional.objects.all().order_by('-pk')
    
class ServicoCreateView(LoginRequiredMixin, TestMixinIsAdmin, CreateView):

    model = Servico
    login_url = 'accounts:login'
    template_name = 'profissionais/cadastro.html'
    fields = ['nome',]
    success_url = reverse_lazy('profissionais:servico_lista')
    
class ServicoListView(LoginRequiredMixin, TestMixinIsAdmin, ListView):
    
    login_url = 'accounts:login'
    template_name = 'profissionais/servico_list.html'

    def get_queryset(self):
        return Servico.objects.all().order_by('-pk')


class AgendaCreateView(LoginRequiredMixin, TestMixinIsAdmin, CreateView):

    model = Agenda
    login_url = 'accounts:login'
    template_name = 'profissionais/agenda_cadastro.html'
    fields = ['profissional', 'dia', 'horario']
    success_url = reverse_lazy('profissionais:agenda_lista')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class AgendaUpdateView(LoginRequiredMixin, TestMixinIsAdmin, UpdateView):

    model = Agenda
    login_url = 'accounts:login'
    template_name = 'profissionais/agenda_cadastro.html'
    fields = ['profissional', 'dia', 'horario']
    success_url = reverse_lazy('profissionais:agenda_lista')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class AgendaDeleteView(LoginRequiredMixin, TestMixinIsAdmin, DeleteView):
    model = Agenda
    success_url = reverse_lazy('profissionais:agenda_lista')
    template_name = 'form_delete.html'

    def get_success_url(self):
        messages.success(self.request, "Agendamento excluída com sucesso!")
        return reverse_lazy('profissionais:agenda_lista')


class AgendaListView(LoginRequiredMixin, TestMixinIsAdmin, ListView):
    
    login_url = 'accounts:login'
    template_name = 'profissionais/agenda_list.html'

    def get_queryset(self):
        return Agenda.objects.filter().order_by('-pk')
    
profissional_cadastro = ProfissionalCreateView.as_view()
profissional_lista = ProfissionalListView.as_view()
servico_cadastro = ServicoCreateView.as_view()
servico_lista = ServicoListView.as_view()
agenda_cadastro = AgendaCreateView.as_view()
agenda_atualizar = AgendaUpdateView.as_view()
agenda_lista = AgendaListView.as_view()
agenda_deletar = AgendaDeleteView.as_view()

