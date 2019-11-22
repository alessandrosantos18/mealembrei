from django.views.generic import TemplateView
from NovoProjeto.models import Paciente, Remedio
from django.views.generic import CreateView
from django.urls.base import reverse_lazy
from django.views.generic.list import ListView

class Index(TemplateView):
    template_name ="index.html"
    
class CriaPaciente(CreateView): 
    template_name = "index.html"   
    model = Paciente()
    fields = '__all__'
    success_url = reverse_lazy("index")
    
class Inicio(TemplateView):
    template_name = "Inicio.html"  
    
    
class Login(CreateView): 
    template_name = "login.html"   
    model = Paciente()
    fields = '__all__'
    success_url = reverse_lazy("index") 
    
      
class Exercicio(TemplateView):
    template_name = "exercicios.html" 
    
class Alimentacao(TemplateView):
    template_name = "alimentacao.html" 
    
class Agenda(TemplateView):
    template_name = "agenda.html" 
    
    
class Remedios(CreateView): 
    template_name = "remedios.html"   
    model = Remedio()
    fields = '__all__'
    success_url = reverse_lazy("lista")   
    
class Lista(ListView):
    template_name = "lista.html"  
    model = Remedio  
    context_object_name = 'remedios'     
    
            
    
    
    
