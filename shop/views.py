from django.shortcuts import render , get_object_or_404 , redirect
from .models import Product , Category 
from comments.models import Comment
from comments.forms import CommentForm
from django.db.models import Q
from django.core.paginator import Paginator


# Create your views here.

def home(request,page=1):
    products_list = Product.objects.filter(available=True,status='p')
    paginator = Paginator(products_list,4)
    products = paginator.get_page(page)
    if 'search' in request.GET:
        search = request.GET['search']
        products = products.filter(Q(name__icontains=search) | Q(description__icontains=search))
    return render(request,'shop/index.html',{'products':products,})


def detail(request,slug):
    product = get_object_or_404(Product,slug=slug,status='p')
    comment = Comment.objects.filter(product=product)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            newcomment = form.save(commit=False)
            newcomment.user = request.user
            newcomment.product = product
            newcomment.save()
    else:
        form = CommentForm()
    return render(request,'shop/detail.html',{'product':product,'comment':comment,'form':form}) 


def category_detail(request,slug):
    category = get_object_or_404(Category,slug=slug)
    product = category.cat.filter(available=True)
    return render(request,'shop/index.html',{'products':product}) 


def add_reply(request,product_slug,comment_pk):
    product = get_object_or_404(Product,slug=product_slug)
    comment = get_object_or_404(Comment,pk=comment_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            newreply = form.save(commit=False)
            newreply.user = request.user
            newreply.product = product
            newreply.reply = comment
            newreply.is_reply = True
            newreply.save()
            return redirect('shop:detail',product_slug)
    return render(request,'shop/replycm_loop.html',{'form':form})


def search(request):
    products = Product.objects.filter(available=True)
    if 'search' in request.GET:
        search = request.GET['search']
        products = products.filter(Q(name__icontains=search) | Q(description__icontains=search))
    return render(request,'shop/index.html',{'products':products,})