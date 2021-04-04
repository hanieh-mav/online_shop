from django.shortcuts import render , get_object_or_404 , redirect  
from .models import Comment
from .forms import CommentForm
from shop.models import Product
from django.views.generic import CreateView
# Create your views here.



 