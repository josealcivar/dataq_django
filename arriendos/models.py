from datetime import datetime
from django.db import models
from cliente.models import Cliente
from empresa.models import Empresa

#{ 'id_cliente': 2, 'id_empresa': 2, 'costo_diario': 5600, 'dias': 4},
# Create your models here.

class Arriendos(models.Model):
    costo_diario = models.BigIntegerField()
    dias = models.IntegerField()
    fecha_arriendo=models.DateField(blank=True,null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {} {} {} {}'.format(self.cliente, self.empresa, self.fecha_arriendo, self.costo_diario, self.dias)