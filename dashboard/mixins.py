from django.shortcuts import render , Http404 , get_object_or_404
from shop.models import Product
    

class AccessUserMixin():
    def dispatch(self, request  ,*args , **kwargs):
        if request.user.is_shopadmin or request.user.is_admin:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("You don't have access to this page")


class FieldMixin():
    def dispatch(self, request , *args , **kwargs):
        if request.user.is_admin:
            self.fields = ['name','slug','category','photo','description','storage','available','price','status']
        elif request.user.is_shopadmin:
            self.fields = ['name','slug','category','photo','description','storage','available','price']
        else:
            Http404("You don't have access to this page")
        return super().dispatch(request,*args,**kwargs)           


class FormValifMixin():
    def form_valid(self,form):
        if self.request.user.is_admin:
            form.save()
        else:
            self.obj = form.save(commit=False)
            self.obj.status = 'd'
        return super().form_valid(form)


class AccessMixin():
    def dispatch(self, request , pk ,*args , **kwargs):
        product = get_object_or_404(Product,pk=pk)
        if request.user.is_shopadmin and product.status == 'd' or request.user.is_admin:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("You don't have access to this page")


class DetailViewMixin(object):
    details_model = None
    context_detail_object_name = None

    def get_context_data(self, **kwargs):
        context = super(DetailViewMixin, self).get_context_data(**kwargs)
        context[self.context_detail_object_name] = self.get_detail_object()
        return context

    def get_detail_object(self):
        return self.details_model._default_manager.get(pk=self.kwargs['pk'])


class AccessDeleteMixin():
    def dispatch(self, request  ,*args , **kwargs):
        if request.user.is_admin:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("You don't have access to this page")