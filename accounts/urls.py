from django.urls import path
from .views import loginUser , LogoutUser , RegisterUser , userorder , user_order_detail

app_name = 'accounts'

urlpatterns = [
    path('login/',loginUser,name='login'),
    path('logout/',LogoutUser,name='logout'),
    path('register/',RegisterUser,name='register'),
    path('order/',userorder,name='user_order'),
    path('order/<int:pk>',user_order_detail,name='user_order_detail'),
]