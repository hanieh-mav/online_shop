from django import template
from ..models import Category
from cart.cart import Cart


register = template.Library()

@register.inclusion_tag('partials/category_navbar.html')
def category_navbar():
    return {
        'category': Category.objects.all()
     }


@register.inclusion_tag('dashboard/partials/link.html')
def link(request , link_name , content , classes):
    return {
        'request' : request ,
        'link_name' : link_name ,
        'link': "dashboard:{}".format(link_name),
        'content' : content ,
        'classes' : classes ,
    }