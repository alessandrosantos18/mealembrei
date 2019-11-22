from django.db import models


class Paciente(models.Model): 
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    
    sobrenome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    
    cpf = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )
    
    celular = models.CharField(
        max_length=11,
        null=False,
        blank=False
    )
    
    TelefoneFixo = models.CharField(
        max_length=8,
        null=False,
        blank=False
    )
    
    email = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )


class Remedio(models.Model): 
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    
    data = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
        
objetos = models.Manager    