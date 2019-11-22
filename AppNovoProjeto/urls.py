from django.urls import path
from AppNovoProjeto.views import Index, Inicio, Login, Exercicio, Agenda, Alimentacao, Remedios,Lista
from AppNovoProjeto.views import CriaPaciente
from NovoProjeto.models import Paciente, Remedio

urlpatterns = [
    path('',Login.as_view(model=Paciente), name="login"), 
    path('paciente/inicio/', CriaPaciente.as_view(model=Paciente), name="index"),
    path('paciente/inicio', Inicio.as_view(), name="inicio"),
    path('inicio/exercicio', Exercicio.as_view(), name="exercicio"),
    path('inicio/agenda', Agenda.as_view(), name="agenda"),
    path('inicio/alimentacao', Alimentacao.as_view(), name="alimentacao"),
    path('inicio/remedios', Remedios.as_view(model=Remedio), name="remedios"),
    path('inicio/remedio/lista',Lista.as_view(),name="lista"),
    
]