from django.urls import path
from . import views
app_name='product'

urlpatterns=[
path('welcome/',views.index,name='index'),
path('product_detail/<slug:product_code>',views.product_detail,name='product_detail'),
path('welcome/<slug:name>',views.category_based,name='category_based'),
]
