from django.urls import path
from .views import detail , create

app_name = 'orders'

urlpatterns = [
    path('<int:order_id>', detail ,name='detail'),
    path('create' , create ,name='create')
]