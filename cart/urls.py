from django.urls import path
from . import views

app_name='cart'

urlpatterns = [
path("",views.cart_detail,name="cart_detail"),
path('add/<slug:product_code>',views.add_product,name='add_product'),
path('remove/<slug:product_code>',views.remove_product,name='remove_product'),
]
