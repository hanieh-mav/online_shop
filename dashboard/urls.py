from django.urls import path
from .views import (ProductList , CreateProduct , PreviewProduct , UpdateProduct , DeleteProduct , OrderList,
OrderDetail , DeleteOrder , UserList , UserDetail , DeleteUser)

app_name = 'dashboard'
urlpatterns = [
    path('',ProductList.as_view(),name='index'),
    path('page/<int:page>',ProductList.as_view(),name='index'),
    path('create', CreateProduct.as_view(), name = 'create'),
    path('preview/<int:pk>', PreviewProduct.as_view(), name = 'preview'),
    path('update/<int:pk>', UpdateProduct.as_view(), name = 'update'),
    path('delete/<int:pk>', DeleteProduct.as_view(), name = 'delete-product'),
    path('order',OrderList.as_view(),name='order'),
    path('order/<int:pk>',OrderDetail.as_view(),name='order-detail'),
    path('delete/order/<int:pk>', DeleteOrder.as_view(), name = 'delete-order'),
    path('user/list', UserList.as_view(), name = 'user-list'),
    path('user/<int:pk>',UserDetail.as_view(),name='user-detail'),
    path('delete/user/<int:pk>', DeleteUser.as_view(), name = 'delete-user'),
    
]
