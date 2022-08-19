from multiprocessing import context
from django.shortcuts import render
from .models import *

# Create your views here.
def store(request):
    productos= Producto.objects.all()
    categorias=Categoria.objects.all()
    ropavieja = productos.filter(categoria__nombre="Ropa vieja")
    
    context={
        'productos':productos,
        'categorias':categorias,
        'ropavieja': ropavieja
    }
    return render(request, 'store/store.html', context)

def cart(request):
    if request.user.is_authenticated:
        cliente =  request.user.cliente
        pedido, created = Pedido.objects.get_or_create(cliente=cliente, enviado=False)
        items =pedido.pedido_item_set.all()
        
    else:
        items=[]
        print("so sorry")
        pedido = {'get_cart_total':0,'get_cart_items':0}
        
    context={'items':items,
             'pedido':pedido}
    return render(request,'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        cliente =  request.user.cliente
        pedido, created = Pedido.objects.get_or_create(cliente=cliente, enviado=False)
        items =pedido.pedido_item_set.all()
        
    else:
        items=[]
        print("so sorry")
        pedido = {'get_cart_total':0,'get_cart_items':0}
        
    context={'items':items,
             'pedido':pedido}
    return render(request, 'store/checkout.html', context)   

# def registerPage(request): 
#     form=CreateUserForm()
#     if request.method=='POST':
#         form=CreateUserForm(request.POST)
#         if form.is_valid():
#             user=form.save()
#             username=form.cleaned_data.get('username')
#             group=Group.objects.get( name="clientes")
#             user.groups.add(group)
#             Clientes.objects.create(
#                 user=user, 
#                 nombre=username
#             )
#             messages.success(request, 'Se ha creado una cuenta para:    ' + username)
#             return redirect('login')
#     context={
#         'form':form
#     }
#     return render(request, 'ventas/register.html', context)