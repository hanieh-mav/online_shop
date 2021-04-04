from django.urls import path
from .views import home , detail , category_detail , add_reply , search

app_name = 'shop'
urlpatterns = [
    path('',home,name='home'),
    path('page/<int:page>',home,name='home'),
    path('search',search,name='search'),
    path('detail/<slug:slug>',detail,name='detail'),
    path('reply/<slug:product_slug>/<int:comment_pk>',add_reply,name='add-reply'),
    path('category/<slug:slug>',category_detail,name='category_detail'), ]
