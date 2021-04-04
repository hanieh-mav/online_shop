from django.urls import path
from .views import cart , cart_add , cart_remove , add_quantity

app_name = 'cart'

urlpatterns = [
    path('' ,cart,name='cart'),
    path('add/<int:product_id>' ,cart_add,name='cart_add'),
    path('add/quantity/<int:product_id>',add_quantity,name='add_quantity'),
    path('remove,<int:product_id>' ,cart_remove,name='cart_remove'),
]