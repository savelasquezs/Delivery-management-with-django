from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *

# Create your views here.
def store(request):
    productos= Producto.objects.all()
    categorias=Categoria.objects.all()
    ropavieja = productos.filter(categoria__nombre="Ropa vieja")
    if request.user.is_authenticated:
        cliente =  request.user.cliente
        pedido, created = Pedido.objects.get_or_create(cliente=cliente, enviado=False)
        items =pedido.pedido_item_set.all()
        cartItems= pedido.get_cart_items
        
        
    else:
        items=[]
        print("so sorry")
        pedido = {'get_cart_total':0,'get_cart_items':0}
        cartItems = pedido['get_cart_items']
    
    context={
        'productos':productos,
        'categorias':categorias,
        'ropavieja': ropavieja,
        'items':items,
        'pedido':pedido,
        'cartItems':cartItems
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

def updateItem(request):
    data = json.loads(request.body)
    productId=data['productId']
    action = data['action']
    
    print('Action: ', action, '/n','ProductId: ', productId)
    
    customer = request.user.cliente
    product = Producto.objects.get(id=productId)
    pedido, created = Pedido.objects.get_or_create(cliente=customer, enviado=False)
    
    pedidoItem, created = Pedido_item.objects.get_or_create(pedido=pedido, producto=product)
    
    if action == 'add':
        pedidoItem.cantidad = (pedidoItem.cantidad + 1)
    elif    action =='remove':
        pedidoItem.cantidad = (pedidoItem.cantidad -1)
        
    pedidoItem.save()
    
    if pedidoItem.cantidad <=0:
        pedidoItem.delete()
    
    return JsonResponse('Item was added', safe=False)