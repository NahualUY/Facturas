from django.db import models

class Cliente(models.Model):
    cedula = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=8)
    email = models.CharField(max_length=255)

    def __unicode__(self):
        return self.nombre + ' ' + self.apellido

class Factura(models.Model):
    numero = models.IntegerField(primary_key=True)
    cliente = models.ForeignKey(Cliente, related_name='facturas', on_delete=models.PROTECT)
    fecha = models.DateField()
    monto = models.DecimalField(decimal_places=2, max_digits=8)
    esta_paga = models.BooleanField(default=False)
