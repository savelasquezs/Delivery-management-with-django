from django.forms import ModelForm
from .models import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1', 'password2']

class ClienteForm(ModelForm):
    class Meta:
        model= Cliente
        fields='__all__'
        
class ProductoForm(ModelForm):
    class Meta:
        model= Producto
        fields='__all__'

class PedidoForm(ModelForm):
    class Meta:
        model= Pedido
        fields='__all__'