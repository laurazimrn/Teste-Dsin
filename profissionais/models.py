import datetime
from datetime import date
from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.db.models.fields.related import ForeignKey

class Servico(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=200)
    
    def __str__(self):
        return f'{self.nome}'
    
class Profissional(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=200)
    email = models.EmailField(verbose_name="Email")
    cpf = models.CharField(verbose_name="CPF", max_length=200)
    phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="O número precisa estar neste formato: \
                    '+99 99 9999-0000'.")

    telefone = models.CharField(verbose_name="Telefone",
                                validators=[phone_regex],
                                max_length=17, null=True, blank=True)
    servico = ForeignKey(Servico,
                               on_delete=models.CASCADE,
                               related_name='profissionais')
    
    def __str__(self):
        return f'{self.nome}'

def validar_dia(value):
    today = date.today()
    weekday = date.fromisoformat(f'{value}').weekday()
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    aftertomorrow = datetime.date.today() + datetime.timedelta(days=2)

    if value < today :
        raise ValidationError('Agendamento pelo sistema somente 2 dias antes .')
    
    if value == today :
        raise ValidationError('Agendamento pelo sistema somente 2 dias antes .')

    if value == tomorrow:
        raise ValidationError('Agendamento pelo sistema somente 2 dias antes .')

    if value == aftertomorrow:
        raise ValidationError('Agendamento pelo sistema somente 2 dias antes .')
    


    if (weekday == 5) or (weekday == 6):
        raise ValidationError('Escolha um dia útil da semana.')


class Agenda(models.Model):
    profissional = ForeignKey(Profissional, on_delete=models.CASCADE, related_name='agenda')
    dia = models.DateField(help_text="Insira uma data para agenda", validators=[validar_dia])
    
    HORARIOS = (
        ("1", "07:00 ás 08:00"),
        ("2", "08:00 ás 09:00"),
        ("3", "09:00 ás 10:00"),
        ("4", "10:00 ás 11:00"),
        ("5", "11:00 ás 12:00"),
    )
    horario = models.CharField(max_length=10, choices=HORARIOS)
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        verbose_name='Usuário', 
        on_delete=models.CASCADE
    )
    class Meta:
        unique_together = ('horario', 'dia')
        
    def __str__(self):
        return f'{self.dia.strftime("%b %d %Y")} - {self.get_horario_display()} - {self.profissional}'