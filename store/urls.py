from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('update_item', views.updateItem, name='update_item'),
    path('create_customer', views.createCustomer, name='create_customer'),
    path('create_product', views.createProduct, name='create_product'),

    
    
]
