from django.contrib import admin
from .models import Category,Products,Relatedimage
# Register your models here.
class category_admin(admin.ModelAdmin):
    list_display=('title','slug','description','category_image','is_active','is_featured')
    list_editable=('slug','is_active','is_featured')
    list_filter=('is_active','is_featured')
    search_fields=('title','description')
    prepopulated_fields={"slug":("title",)}

admin.site.register(Category,category_admin)

class related_admin(admin.StackedInline):
    model=Relatedimage

class product_admin(admin.ModelAdmin):
    list_display=('title','slug','description','product_image','product_stock','price','category','is_active','is_featured')
    list_editable=('price','product_stock','slug','is_active','is_featured')
    list_filter=('is_featured','is_active')
    search_fields=('title','description')
    prepopulated_fields={'slug':('title',)}
    inlines=[related_admin]
admin.site.register(Products,product_admin)