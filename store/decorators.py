from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('store')
        else:
            return view_func(request, *args, **kwargs)
        
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args, **kwargs):
            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
            if group in allowed_roles:
                print(request.user.groups)
                print(request.user.groups.all())  
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('Lo siento, no tienes permiso para ingresar a esta pagina')
            print("working",allowed_roles )
            return view_func(request,*args, **kwargs)
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group=None
        if request.user.groups.exists():
            group=request.user.groups.all()[0].name
        if group=='admin':
            return view_func(request, *args, **kwargs)
        if group=='delivery':
            return redirect('delivery_page')
    return wrapper_function  