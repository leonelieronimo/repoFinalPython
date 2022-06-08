import datetime
from django import forms
from django.forms import ModelForm
from app_coder.models import Cliente


class PedidosForm(forms.Form):
    name = forms.CharField(max_length=40, min_length=3, label='Nombre')
    last_name = forms.CharField(max_length=40, min_length=3, label='Apellido')
    telephone = forms.IntegerField(label='Celular')
    respuesto = forms.CharField(max_length=40, min_length=3, label='Tipo Respuesto')


class ClienteForm(forms.Form):
    name = forms.CharField(max_length=40, min_length=3, label='Nombre')
    last_name = forms.CharField(max_length=40, label='Apellido')
    email = forms.EmailField(label='Correo electrónico')
    cuit = forms.IntegerField(label='CUIT')

# class ProfesorForm(ModelForm):
#     class Meta:
#         model = Profesor
#         fields = '__all__'


class EnviosForm(forms.Form):
    name = forms.CharField(max_length=40, min_length=3, label='Nombre')
    last_name = forms.CharField(max_length=40, min_length=3, label='Apellido')
    city = forms.CharField(max_length=40, min_length=3, label='Ciudad')
    adress = forms.CharField(max_length=40, min_length=3, label='Direccion')
    telephone = forms.IntegerField(label='Telefono/Celular')
    code_postal = forms.IntegerField(label='Codigo Postal')
    due_date = forms.DateField(
        label='Fecha de Entrega',
        widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'})
    )
    is_delivered = forms.BooleanField(label='Entregado', required=False)
