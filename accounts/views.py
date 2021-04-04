from django.shortcuts import render , redirect , get_object_or_404
from .forms import LoginUserForm , RegisterUserForm
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User
from orders.models import Order

# Create your views here.

def loginUser(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,email = cd['email'],password = cd['password'])
            if user is not None:
                login(request,user)
                messages.success(request, 'you logged in successfully', 'success')
                if user.is_admin or user.is_shopadmin :
                    return redirect('dashboard:index')
                else:
                    return redirect('shop:home')
            else:
                messages.error(request, 'username or password is wrong', 'danger')    
    else:
        form = LoginUserForm()    
    return render(request,'accounts/login.html',{'form':form})   


def LogoutUser(request):
    logout(request)
    return redirect('shop:home')


def RegisterUser(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['password1'] and cd['password2'] and cd['password1'] == cd['password2']:
                if User.object.filter(email=cd['email']).exists():
                    messages.error(request, 'This email already exists', 'danger') 
                else:
                    if User.object.filter(phone=cd['phone']).exists():
                        messages.error(request, 'This phone already exists', 'danger') 
                    else:
                        user = User.object.create_user(email=cd['email'],first_name=cd['firstname'],last_name=cd['lastname'],
                        password=cd['password1'],phone=['phone'])
                        user.save()
                        messages.success(request, 'you registered successfully', 'success')
                        return redirect('shop:home')
            else:
                messages.error(request, 'Passwords must be match', 'danger') 
    else:
        form = RegisterUserForm()
    return render(request,'accounts/register.html',{'form':form})

@login_required
def userorder(request):
    user = request.user
    orders = Order.objects.filter(user=user)
    return render(request,'accounts/order-list.html',{'orders':orders})

@login_required
def user_order_detail(request,pk):
    order = get_object_or_404(Order,pk=pk)
    return render(request,'accounts/order-detail.html',{'order':order})