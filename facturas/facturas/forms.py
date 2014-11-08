from django import forms
import models

class AgregarClienteForm(forms.Form):
    cedula = forms.RegexField(regex='^[0-9\\.-]*$')
    nombre = forms.CharField(required=False)
    apellido = forms.CharField(required=False)
    telefono = forms.CharField(required=False)
    email = forms.EmailField()


class AgregarFacturaForm(forms.Form):
    numero = forms.IntegerField()
    cliente = forms.ModelChoiceField(queryset=None)
    producto = forms.ModelChoiceField(queryset=None)
    fecha = forms.DateField()
    monto = forms.CharField(required=False)
    esta_paga = forms.BooleanField(required=False)

    def __init__(self, database, *args, **kwargs):
        super(AgregarFacturaForm, self).__init__(*args, **kwargs)

        self.fields['cliente'].queryset = models.Cliente.objects.using(database).all()
        self.fields['producto'].queryset = models.Producto.objects.using(database).all()
