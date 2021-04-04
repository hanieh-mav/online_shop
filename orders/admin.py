from django.contrib import admin
from .models import Order , OrderItem

# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ('product',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk','user','created','updated','is_paid')
    list_filter = ('is_paid',)
    inlines = (OrderItemInline,)