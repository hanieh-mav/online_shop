from django.shortcuts import render, get_object_or_404 , redirect
from .cart import Cart
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from shop.models import Product
# Create your views here.

@login_required
def cart(request):
    cart = Cart(request)
    return render(request,'cart/cart.html',{'cart':cart})

@login_required
@require_POST
def cart_add(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(Product,pk=product_id)
    quantity = request.POST['quantity']
    quantity = int(quantity)
    cart.add(product=product,quantity=quantity)
    return redirect('cart:cart')


@login_required
@require_POST
def add_quantity(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(Product,pk=product_id)
    quantity = request.POST['quantity']
    quantity = int(quantity)
    cart.add_quantity(product=product,quantity=quantity)
    return redirect('cart:cart')

@login_required
def cart_remove(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(Product,pk=product_id)
    cart.remove(product)
    return redirect('cart:cart')

