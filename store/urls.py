from django.urls import path
from . import views

urlpatterns = [
    
    path("register", views.registerPage, name="register"),
    path("login", views.loginPage, name="login"),
    path("logout", views.logoutPage, name="logout"),
    
    
    path("delivery", views.delivery, name="delivery_page"),  
    
    
    
    path('', views.store, name='store'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('update_item', views.updateItem, name='update_item'),
    path('process_order', views.processOrder, name='process_order'),
    
    path('update_order_customer', views.updateOrderCustomer, name='update_order_customer'),
    
    
    path('create_customer', views.createCustomer, name='create_customer'),
    path("update_cliente/<str:pk>", views.updateCliente, name="update_cliente"),
    path("borrar_cliente/<str:pk>", views.deleteCliente, name="borrar_cliente"),   
    
    path('create_product', views.createProduct, name='create_product'),
    path("update_producto/<str:pk>", views.updateProducto, name="update_producto"),
    path("borrar_producto/<str:pk>", views.deleteProducto, name="borrar_producto"), 
    
    path("borrar_producto/<str:pk>", views.deleteProducto, name="borrar_producto"),   
    
      
    
    
    
    
    
]
