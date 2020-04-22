from django.shortcuts import render, get_object_or_404 , redirect
from django.views.decorators.http import require_POST
from .forms import CartAddProductForm
from .cart import Cart
from product.models import Product
# Create your views here.
@require_POST
def add_product(request,product_code):
    cart =Cart(request)
    form=CartAddProductForm(request.POST)

    product=get_object_or_404(Product,product_code=product_code)
    print("inside ad_product")
    if form.is_valid():
        form_val=form.cleaned_data
        cart.add(product=product,
                quantity=form_val['quantity'])
    print("ended add_product")
    return redirect('cart:cart_detail')

# @require_POST
def remove_product(request,product_code):
    cart=Cart(request)
    product=get_object_or_404(Product,product_code=product_code)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart=Cart(request)
    print("inside cart_Detail")
    for item in cart:
            item['update_quantity_form'] = CartAddProductForm(
                              initial={'quantity': item['quantity'],
                              'update': True})
    return render(request,
                    'detail.html',
                    {'cart':cart})
