from django import forms
import models

class AgregarClienteForm(forms.Form):
    cedula = forms.RegexField(regex='^[0-9]{7}$')
    nombre = forms.CharField(required=False)
    apellido = forms.CharField(required=False)
    telefono = forms.CharField(required=False)
    email = forms.EmailField()


class AgregarFacturaForm(forms.Form):
    numero = forms.IntegerField()
    cliente = forms.ModelChoiceField(queryset=models.Cliente.objects.all())
    fecha = forms.DateField()
    monto = forms.DecimalField()
    esta_paga = forms.BooleanField(required=False)