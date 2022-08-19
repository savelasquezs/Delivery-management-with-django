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
    context={}
    return render(request,'store/cart.html', context)

def checkout(request):
    context={}
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