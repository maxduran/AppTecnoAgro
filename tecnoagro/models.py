from django.db import models
from django.utils import timezone


# Create your models here.
 
'''class Consulta(models.Model):
   nombre = models.ForeignKey('auth.User', on_delete=models.CASCADE)
   email = models.CharField(max_length=200)
   mensaje = models.TextField()
   create_date = models.DateTimeField(default=timezone.now)
   publish_date = models.DateTimeField(blank=True, null=True)
 
   def publish(self):
       self.publish_date = timezone.now()
       self.save()
 
   def __str__(self):
       return self.nombre'''

class Consulta(models.Model):
    nombre = models.CharField(max_length=60)
    email = models.CharField(max_length=50)
    mensaje = models.CharField(max_length=120)
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre
        
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    telefono =models.IntegerField()
    direccion = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre