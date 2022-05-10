from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.
def product_list(request):
    if request.session.has_key('staff'):
        products = Product.objects.filter(is_active=True)
        form = ProductForm()
        context = {
            'products' : products,
            'form':form
        }
        return render(request,'product_module/index.html',context)
    else:
        return redirect('/login')

def add_product(request):
    if request.method=="POST":
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            print("hi")
            form.save()
            return redirect('/products')
        else:
            error ="Please fill correctly"
            return render(request,'product_module/index.html',{'form':form,'error':error})

def edit_product(request,pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method=="POST":
        form = ProductForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return redirect('/products')
    else:
        return render(request,'product_module/edit_product.html',{'form':form})
    
def delete_product(request,pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect('/products')


