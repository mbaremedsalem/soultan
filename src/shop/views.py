from multiprocessing import context
from django.shortcuts import render
from .models import  Category,Order, Product
from django.core.paginator import Paginator
from .forms import OrderForm,ProductForm
# Create your views here.

def index(request):
    product_object = Product.objects.all()  
    if request.method=="POST":
        form = ProductForm(request.POST)
        if form.is_valid():
           myform = form.save()
    else:
        form = ProductForm()
    return render(request,'shop/index.html',{'product_object':product_object})
def category(request):
    category_object = Category.objects.all()
    return render(request,'shop/detail.html',{'category_object':category_object })
def detail(request, myid):
    product_object = Product.objects.get(id=myid)
    return render(request,'shop/detail.html',{'product':product_object})

def cart(request):
    context={}
    return render(request,'shop/cart.html',context)

def check(request):
    if request.method=="POST":
        form = OrderForm(request.POST)
        if form.is_valid():
           myform = form.save()
    else:
        form = OrderForm()
        
    return render(request,'shop/checkout.html',{'form':form})    

def contact(request):
    context={}
    return render(request,'shop/demo3-contact.html',context)     

def about(request):
    context={}
    return render(request,'shop/about.html',context)      