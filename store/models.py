
from email.policy import default
from django.db import models
from django.contrib.auth.models import  User


class Usuario(models.Model):
    usuario = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200, null=True)
    telefono = models.CharField(max_length=200, null=True)
    direccion = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nombre
    

class Cliente(models.Model):
    nombre = models.CharField(max_length=200, null=True)
    telefono = models.CharField(max_length=200, null=True)
    direccion = models.CharField(max_length=200, null=True, blank=True)
    valor_domi = models.IntegerField(default=0)
    pet_particulares = models.CharField( max_length=250, null=True, blank=True)
    
    def __str__(self):
        return self.nombre
    
class Domiciliario(models.Model):
    usuario = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200, null=True)
    telefono = models.CharField(max_length=200, null=True)

    def __str__(self):
            return self.nombre

    
    
class Categoria(models.Model):
    nombre = models.CharField( max_length=100)
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=200, default="")
    precio = models.IntegerField(default=0, null=False, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, blank=True, null=True)
    imagen = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.nombre
    
    @property
    def imagenURL(self):
        try:
            url= self.imagen.url
        except:
            url =""
        return url

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_tomado = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=200, null=True)
    enviado = models.BooleanField(default=False, null=True, blank=False)
    tomado = models.BooleanField(default=False, null=True, blank=False)
    
    def __str__(self):
        return str(self.transaction_id) + str(self.cliente)
    
    
    
    @property
    def get_cart_total(self):
        orderitems = self.pedido_item_set.all()
        total=sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.pedido_item_set.all()
        total=sum([item.cantidad for item in orderitems])
        return total
    
    def save(self, *args, **kwargs):
        context = super().save(*args, **kwargs)
        return context
    
class Pedido_item(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True, blank=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True, blank=True)
    cantidad= models.IntegerField(default=0, blank=True, null=True)
    
    @property
    def get_total(self):
        total=self.producto.precio * self.cantidad
        return total 
    
    def save(self, *args, **kwargs):
        context = super().save(*args, **kwargs)
        return context
    
class Envio (models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True, blank=True)
    direccion = models.CharField(max_length=200,default="para llevar" )
    telefono = models.CharField(max_length=200,default="0" )
    nombre = models.CharField(max_length=200,default="sin nombre" )
    valor_domi = models.IntegerField(default=0)   
    domiciliario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_envio = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField(default=0)
    
    def __str__(self):
        return self.direccion
    
class Abonos(models.Model):
    domiciliario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)
    valor=models.IntegerField(default=0)
    fecha_abono = models.DateTimeField(auto_now_add=True)
    
    
    
        
    
    
    

# Create your models here.
