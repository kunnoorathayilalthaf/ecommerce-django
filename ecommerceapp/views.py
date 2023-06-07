from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Category,Products,Relatedimage,contactform,Cart
from .forms import SignUp
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import loginForm
from django.core.mail import send_mail
from django.conf import settings
import decimal
from django.contrib.auth.decorators import login_required


# Create your views here.
def home_function(request):
    return render(request,'index.html')

def blog_function(request):
    return render(request,'blog.html')

def contact_function(request):
    if request.method == 'POST':
        email=request.POST['email']
        message=request.POST['msg']
        contactform(email=email,message=message).save()
        send_mail(subject='thankyou',message='thankyou for contacting us',from_email=settings.EMAIL_HOST_USER,recipient_list=[email,],fail_silently=False)
        messages.success(request,'Message sent')

    return render(request,'contact.html')

def about_function(request):
    return render(request,'about.html')

def category_function(request):
    categories=Category.objects.filter(is_active=True)
    return render(request,'category.html',{'categories':categories})

def product_function(request,slug):
    category=get_object_or_404(Category,slug=slug)
    products=Products.objects.filter(is_active=True,category=category)
    context={'category':category,'products':products}
    return render(request,'product.html',context)
@login_required
def shoppingcart_function(request):
    user=request.user
    cart_products=Cart.objects.filter(user=user)
    amount=decimal.Decimal(0)
    shipping_amount=decimal.Decimal(10)
    cp=[p for p in Cart.objects.all() if p.user==user]
    if cp:
        for p in cp:
            
            temp_amount=(p.quantity*p.product.price)
            amount+=temp_amount
    context={
        'cart_products':cart_products,'amount':amount,'shipping_amount':shipping_amount,'total_amount':amount+shipping_amount
    }


    return render(request,'shopping-cart.html',context)

@login_required
def add_to_cart(request):
    user=request.user
    product_id=request.GET.get('prod_id')
    product=get_object_or_404(Products,id=product_id)

    item_already_in_cart=Cart.objects.filter(product=product_id,user=user)
    if item_already_in_cart:
        cp=get_object_or_404(Cart,product=product_id,user=user)
        cp.quantity += 1
        cp.save()
    else:
        Cart(user=user,product=product).save()
    return redirect('shoppingcart')

@login_required
def pluscart(request,cart_id):
    if request.method == 'GET':
        cp=get_object_or_404(Cart,id=cart_id)
        cp.quantity +=1
        if cp.quantity <= cp.product.product_stock:
            cp.save()
    return redirect('shoppingcart')

@login_required
def minuscart(request,cart_id):
    if request.method == 'GET':
        cp=get_object_or_404(Cart,id=cart_id)
        if cp.quantity ==1:
            cp.delete()
        else:
            cp.quantity -=1
            cp.save()
    return redirect('shoppingcart')
@login_required
def removecart(request,cart_id):
    if request.method == 'GET':
        cp=get_object_or_404(Cart,id=cart_id)
        if cp.quantity <= cp.product.product_stock:
            cp.delete()
    return redirect('shoppingcart')


def productdetail_function(request,slug):
    products=get_object_or_404(Products,slug=slug)
    related_img=Relatedimage.objects.filter(products=products.id)
    context={'products':products,'related_img':related_img}
    return render(request,'product-detail.html',context)

def signup_function(request):
    if request.method=='POST':
        form=SignUp(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.save()
            messages.success(request,'Registered successfully')
        else:
            messages.error(request,'Registration failed')
    else:
        form=SignUp()
    context={'form':form}
    return render(request,'signup.html',context)

def login_function(request):
    if request.method == 'POST':
        form=loginForm(request.POST)
        username=form['username'].value()
        password=form['password'].value()
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.info(request,'login success')
            return redirect('/')
        else:
            messages.info(request,'invalid')
    else:
        form=loginForm()
    context={'form':form}

    return render(request,'login.html',context)

def logout_function(request):
   logout(request)
   return redirect('/')

def search_function(request):
    q = request.GET.get('q','')
    data=Products.objects.filter(title__icontains=q).order_by('-id')
    context={"data":data}
    return render(request,'search.html',context)


