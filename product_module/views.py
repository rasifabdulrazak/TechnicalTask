from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.
def product_list(request):
    products = Product.objects.filter(is_active=True)
    form = ProductForm()
    context = {
        'products' : products,
        'form':form
    }
    return render(request,'product_module/index.html',context)