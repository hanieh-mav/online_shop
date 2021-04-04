from django.shortcuts import render , redirect , Http404 , get_object_or_404 
from django.urls import reverse_lazy
from django.views.generic import (CreateView , ListView , DetailView , UpdateView , DeleteView)
from shop.models import Product
from .mixins import (AccessUserMixin,FieldMixin , FormValifMixin , AccessMixin , DetailViewMixin ,
AccessDeleteMixin )
from orders.models import Order 
from accounts.models import User
# Create your views here.

class ProductList(ListView):
    template_name = 'dashboard/product_list.html'
    paginate_by = 6
    def get_queryset(self):
        if self.request.user.is_admin or self.request.user.is_shopadmin:
            return Product.objects.all()
        else:
            raise Http404("You don't have access to this page")


class CreateProduct(AccessUserMixin,FieldMixin,FormValifMixin,CreateView):
    model = Product
    template_name = 'dashboard/product_create.html'


class PreviewProduct(AccessUserMixin,DetailView):
    template_name = 'shop/detail.html'
    def get_object(self):
        pk = self.kwargs.get('pk')
        global product
        product  = get_object_or_404(Product,pk=pk)
        return product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = product
        return context


class UpdateProduct(AccessMixin,FieldMixin,FormValifMixin,UpdateView):
    model = Product
    template_name = 'dashboard/product_create.html'


class DeleteProduct(AccessMixin,DeleteView):
    model = Product
    template_name = 'dashboard/delete.html'
    success_url = reverse_lazy('dashboard:index')


class OrderList(ListView):
    template_name = 'dashboard/order_list.html'
    paginate_by = 6
    def get_queryset(self):
        if self.request.user.is_admin or self.request.user.is_shopadmin:
            return Order.objects.all()
        else:
            raise Http404("You don't have access to this page")


class OrderDetail(AccessUserMixin,DetailViewMixin, UpdateView):
    details_model = Order
    context_detail_object_name = 'order_item'
    model = Order
    template_name = 'dashboard/orderdetail.html'
    fields = ['status']


class DeleteOrder(AccessDeleteMixin,DeleteView):
    model = Order
    template_name = 'dashboard/delete.html'
    success_url = reverse_lazy('dashboard:order')


class UserList(AccessDeleteMixin,ListView):
    template_name = 'dashboard/access_user.html'
    paginate_by = 6
    def get_queryset(self):
        if self.request.user.is_admin:
            return User.objects.all()
        else:
            raise Http404("You don't have access to this page")


class UserDetail(AccessDeleteMixin,DetailViewMixin, UpdateView):
    details_model = User
    context_detail_object_name = 'user'
    model = User
    template_name = 'dashboard/detail_user.html'
    fields = ['is_shopadmin']


class DeleteUser(AccessDeleteMixin,DeleteView):
    model = User
    template_name = 'dashboard/delete.html'
    success_url = reverse_lazy('dashboard:user-list')