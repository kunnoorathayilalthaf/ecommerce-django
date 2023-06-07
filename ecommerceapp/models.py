from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=250,verbose_name="Category_title")
    slug=models.SlugField(max_length=55,verbose_name="Category_slug")
    description=models.TextField(blank=True,verbose_name="Category_description")
    category_image=models.ImageField(upload_to="category",blank=True,null=True,verbose_name="Category_image")
    is_active=models.BooleanField(verbose_name="Is_active")
    is_featured=models.BooleanField(verbose_name="Is_featured")

    def __str__(self):
        return '{}'.format(self.title)
    
    

class Products(models.Model):
    title=models.CharField(max_length=150,verbose_name="Product title")
    slug=models.SlugField(max_length=150,verbose_name="Product slug")
    description=models.TextField(blank=True,verbose_name="Product description")
    product_image=models.ImageField(upload_to="product",blank=True,null=True,verbose_name="Product image")
    product_stock=models.PositiveIntegerField()
    price=models.DecimalField(max_digits=8,decimal_places=2)
    category=models.ForeignKey(Category, verbose_name="product categoy",on_delete=models.CASCADE)
    is_active=models.BooleanField(verbose_name="Is active")
    is_featured=models.BooleanField(verbose_name="Is featured")

    def __str__(self):
        return '{}'.format(self.title)
    
class Relatedimage(models.Model):
    products=models.ForeignKey(Products,default=None,on_delete=models.CASCADE)
    image=models.FileField(upload_to='relimage',null=True)

class contactform(models.Model):
    email=models.EmailField()
    message=models.TextField(blank=True,verbose_name="messege")

class Cart(models.Model):
    user=models.ForeignKey(User,verbose_name='User',on_delete=models.CASCADE)
    product=models.ForeignKey(Products,verbose_name='Product',on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1,verbose_name='quantity')
    
    def __str__(self):
        return str(self.user)
    @property
    def total_price(self):
        return self.quantity*self.product.price
