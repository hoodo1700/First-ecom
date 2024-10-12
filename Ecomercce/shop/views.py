from django.shortcuts import render,get_object_or_404,redirect
from .models import Product,Cart,CartItem,poromotion
from django.db import models

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Cart, CartItem, Category

def index(request):
    products = Product.objects.all()
    lastproducts = Product.objects.all()[:4]
    poromotions = poromotion.objects.all()
    cart_items_count = count_cart_items(request)
    return render(request, 'index.html', {'products': products,'cart_items_count':cart_items_count,'lastproducts':lastproducts,'poromotions':poromotions})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('view_cart')

@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.all()
    cart_items_count = count_cart_items(request)
    total = sum(item.total_price for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total,'cart_items_count':cart_items_count})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})

def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'category_products.html', {'category': category, 'products': products})

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, cart__user=request.user)
    cart_item.delete()
    return redirect('view_cart')

@login_required
def update_cart_item(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, cart__user=request.user)
    quantity = int(request.POST.get('quantity', 1))
    if quantity > 0:
        cart_item.quantity = quantity
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('view_cart')
    
def count_cart_items(request):
    try:
        cart = Cart.objects.get(user=request.user)
        return cart.cartitem_set.aggregate(total_items=models.Sum('quantity'))['total_items'] or 0
    except Cart.DoesNotExist:
        return 0
def electronic(request):
    products = Product.objects.filter(category__name='Electronic Tools')
    return render(request, 'electronic.html', {'products': products})
   




def headphones(request):
    products = Product.objects.filter(category__name='Headphones')
    return render(request, 'headphones.html', {'products': products})

def mobiles(request):
    products = Product.objects.filter(category__name='Apple Phones')
    return render(request, 'mobiles.html', {'products': products})

def samsungphone(request):
    products = Product.objects.filter(category__name='Samsung Phones')
    return render(request, 'samsungphone.html', {'products': products})

def remove_from_cart(request,product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item = CartItem.objects.get(cart=cart, product=product)
    cart_item.delete()
    return redirect('view_cart')
def get_poromotion(request):
    poromotions = poromotion.objects.all()
    return render(request, 'flash_sale.html', {'poromotions': poromotions})


    
