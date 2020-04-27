from django.shortcuts import render,get_object_or_404
from .models import Category,Product
from cart.forms import CartAddProductForm
from mysite.settings import helper
# Create your views here.
def index(request):
    category_list=Category.objects.all()
    products=Product.objects.all()
    return render(request,
                    "home.html",
                    {
                    'products':products,
                    'category_list':category_list,
                    'helper':helper,
                    }
                    )

def product_detail(request,product_code):
    product=get_object_or_404(Product,product_code=product_code)
    category_chosen=get_object_or_404(Category,name=product.category)
    similar_products=category_chosen.products.all()
    cart_product_form=CartAddProductForm()
    return render(request,
                    'product_detail.html',
                    {'product':product,
                    'category_chosen':category_chosen,
                    'similar_products':similar_products,
                    'cart_product_form':cart_product_form,
                    'helper':helper,
                    }
    )

def category_based(request,name):
    category_chosen=get_object_or_404(Category,name=name)
    product_list=category_chosen.products.all()
    return render(request,
                    "category_based.html",

                    {
                    'product_list':product_list,
                    'helper':helper,})
