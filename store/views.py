from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Q
import json
from .models import *
from .forms import *

# Create your views here.
def store(request):
    productos= Producto.objects.all()
    categorias=Categoria.objects.all()
    ropavieja = productos.filter(categoria__nombre="Ropa vieja")
    pedido, created = Pedido.objects.get_or_create( enviado=False)
    items =pedido.pedido_item_set.all()
    cartItems= pedido.get_cart_items
 
    clientes= Cliente.objects.all()
    busqueda = request.GET.get("buscar")
    
    if busqueda:
        clientes = Cliente.objects.filter(
            Q(nombre__icontains=busqueda) |
            Q(direccion__icontains=busqueda) |
            Q(telefono__icontains=busqueda) 
        ).distinct()
   
    
    context={
        'productos':productos,
        'categorias':categorias,
        'ropavieja': ropavieja,
        'items':items,
        'pedido':pedido,
        'cartItems':cartItems,
        'clientes':clientes,
    }
    return render(request, 'store/store.html', context)



def cart(request):
    
    pedido, created = Pedido.objects.get_or_create( enviado=False)
    items =pedido.pedido_item_set.all()
        
    
        
    context={'items':items,
             'pedido':pedido}
    return render(request,'store/cart.html', context)

def checkout(request):
    
    pedido, created = Pedido.objects.get_or_create(enviado=False)
    items =pedido.pedido_item_set.all()
    
    
        
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
    product = Producto.objects.get(id=productId)
    pedido, created = Pedido.objects.get_or_create( enviado=False)
    pedidoItem, created = Pedido_item.objects.get_or_create(pedido=pedido, producto=product)
    if action == 'add':
        pedidoItem.cantidad = (pedidoItem.cantidad + 1)
    elif    action =='remove':
        pedidoItem.cantidad = (pedidoItem.cantidad -1)
    pedidoItem.save()
    if pedidoItem.cantidad <=0:
        pedidoItem.delete()
    return JsonResponse('Item was added', safe=False)

def updateOrderCustomer(request):
    data = json.loads(request.body)
    clienteId=data['clienteId']
    action = data['action']
    print('Action: ', action, '/n','ClienteId: ', clienteId)
    cliente = Cliente.objects.get(id=clienteId)
    pedido, created = Pedido.objects.get_or_create( enviado=False)
   
    if action == 'add':
        pedido.cliente=cliente
    elif    action =='remove':
        pedido.cliente.remove()
    # pedido.save()
    
    return JsonResponse('Customer was added', safe=False)

def createCustomer(request):
    clientes= Cliente.objects.all()
    form=ClienteForm()
    if request.method=="POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_customer')
            
    context={
        'form':form,
        'clientes':clientes
    }
    
    return render(request, 'store/customer_form.html', context)

def  updateCliente(request, pk):
    cliente=Cliente.objects.get(id=pk)
    clientes= Cliente.objects.all()
    form=ClienteForm(instance=cliente)
    if request.method=='POST':
        form=ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('create_customer')
    context={
        'form':form,
        'cliente':cliente,
        'clientes':clientes
    } 
    return render(request, 'store/customer_form.html', context)  

def deleteCliente(request, pk):
    cliente=Cliente.objects.get(id=pk)
    if request.method=='POST':
        cliente.delete()
        return redirect('create_customer')
    context={
        'item':cliente
    }
    return render(request, 'store/borrar.html', context)

def createProduct(request):
    productos= Producto.objects.all()
    form = ProductoForm()
    if request.method=="POST":
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('create_product')
        else:
            print("so sorry")
    else:
        print('algo falló')
    context={
        'form':form,
        'productos':productos
    }
    return render(request, 'store/products_form.html', context)

def  updateProducto(request, pk):
    producto=Producto.objects.get(id=pk)
    productos= Producto.objects.all()
    form=ProductoForm(instance=producto)
    if request.method=='POST':
        form=ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('create_product')
    context={
        'form':form,
        'producto':producto,
        'productos':productos
    } 
    return render(request, 'store/products_form.html', context)  

def deleteProducto(request, pk):
    producto=Producto.objects.get(id=pk)
    if request.method=='POST':
        producto.delete()
        return redirect('create_customer')
    context={
        'item':producto
    }
    return render(request, 'store/borrar.html', context)