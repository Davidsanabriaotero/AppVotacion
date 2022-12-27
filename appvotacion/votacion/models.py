from django.db import models
from django.contrib.auth.models import User

class votacion(models.Model):
    ide=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100,null=False,blank=False,verbose_name="Nombre Votación")
    descripcion = models.CharField(max_length=250,null=False,blank=False,verbose_name="Descripción Votación")
    fecha_inicio = models.DateTimeField(verbose_name="Fecha de Inicio")
    fecha_fin = models.DateTimeField(verbose_name="Fecha de Finalización")
    estado = models.BooleanField(default=True,verbose_name="Estado")
    propietario = models.ForeignKey(User,on_delete= models.CASCADE, null=False, blank=False,verbose_name="Propietario")

    class Meta:
        verbose_name = 'Votación'
        verbose_name_plural = 'Votaciones'
    
    def __str__(self):
        return self.nombre

class votante(models.Model):
    ide = models.IntegerField(primary_key=True,null=False,verbose_name="Identificacion")
    nombre = models.CharField(max_length=50,null=False,blank=False,verbose_name="Nombres")
    apellido = models.CharField(max_length=50,null=False,blank=False,verbose_name="Apellidos")
    votacion = models.JSONField(verbose_name="Votaciones",null=True,blank=True)

    class Meta:
        verbose_name = 'Votante'
        verbose_name_plural = 'Votantes'

    def __str__(self):
        return self.nombre + self.apellido

class candidato(models.Model):
    ide=models.AutoField(primary_key=True)
    votante = models.ForeignKey(votante,on_delete= models.CASCADE, null=False, blank=False,verbose_name="Candidato")
    tarjeton = models.CharField(max_length=4,verbose_name="Número de Tarjeton")
    imagen = models.ImageField(verbose_name="Imagen",null=True)
    descripcion = models.CharField(max_length=100,verbose_name="Descripción")
    votacion = models.ForeignKey(votacion,on_delete= models.CASCADE, null=False, blank=False,verbose_name="Votación")

    class Meta:
        verbose_name = 'Candidato'
        verbose_name_plural = 'Candidatos'

    def __str__(self):
        return self.votante.nombre+str(" ")+self.tarjeton

class votos(models.Model):
    ide=models.AutoField(primary_key=True)
    votacion = models.ForeignKey(votacion,on_delete= models.CASCADE, null=False, blank=False,verbose_name="Votación")
    candidato = models.ForeignKey(candidato,on_delete= models.CASCADE, null=False, blank=False,verbose_name="Votación")
    votante = models.OneToOneField(votante, on_delete= models.CASCADE, null=False, blank=False,verbose_name="Votante")

    def __str__(self):
        return self.votacion.nombre
    