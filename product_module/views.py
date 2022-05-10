from django.shortcuts import render,redirect
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

def add_product(request):
    if request.method=="POST":
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            print("hi")
            form.save()
            return redirect('/products')
        else:
            return redirect('/products')

