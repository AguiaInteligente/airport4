from django.db import models

class lora(models.Model):
     ids = models.TextField(max_length=3)
     alerta = models.IntegerField()
     humidade_ar = models.FloatField()
     temperatura = models.FloatField()
     humidade_solo = models.IntegerField()
     presenca_agua = models.IntegerField()
     gas = models.IntegerField()
     dataleitura = models.DateTimeField(auto_now_add=True, blank=True)

     def __str__(self):
         return self.dataleitura
