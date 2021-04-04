from django.db import models
from django.utils.html import format_html
from django.shortcuts import reverse

# Create your models here.

class CategoryManager(models.Manager):
    def subcategory(self):
        return self.filter(is_subcat = True)

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True)
    subcat = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='scat')
    is_subcat = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']  
        verbose_name_plural = 'categories'

    objects = CategoryManager()

class Product(models.Model):
    STATUS_CHOICES = (
        ('d','draft'),
        ('p','published')
    )
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True)
    category = models.ManyToManyField(Category,related_name='cat')
    photo = models.ImageField(upload_to = 'product/%Y/%M/%d')
    description = models.TextField()
    storage = models.IntegerField()
    available = models.BooleanField(default=True)
    price = models.IntegerField()
    status = models.CharField(max_length=1,choices=STATUS_CHOICES,default='d')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    
    class Meta:
        ordering = ['status','-created'] 
        
    def __str__(self):
        return self.name

    def image_tag(self):
        return format_html("<img src='{}' width =60 height=50>".format(self.photo.url))
    image_tag.short_description = 'photo'    


    def category_to_str(self):
        return '-'.join([category.name for category in self.category.all()])


    def get_absolute_url(self):
        return reverse('dashboard:index')