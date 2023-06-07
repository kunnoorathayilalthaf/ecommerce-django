from django.urls import path
from . import views

urlpatterns=[
    path('',views.home_function,name='home'),
    path('blog',views.blog_function,name='blog'),
    path('about',views.about_function,name='about'),
    path('contact',views.contact_function,name='contact'),
    path('category',views.category_function,name='category'),
    path('<slug:slug>/',views.product_function,name='product'),
    path('products/<slug:slug>/',views.productdetail_function,name='productdetail'),
    path('shoppingcart',views.shoppingcart_function,name='shoppingcart'),
    path('signup',views.signup_function,name='signup'),
    path('login',views.login_function,name='login'),
    path('add_to_cart',views.add_to_cart,name='add_to_cart'),
    path('pluscart/<int:cart_id>/',views.pluscart,name='pluscart'),
    path('minuscart/<int:cart_id>/',views.minuscart,name='minuscart'),
    path('removecart/<int:cart_id>/',views.removecart,name='removecart'),
    path('logout',views.logout_function,name='logout_function'),
    path('search',views.search_function,name='search'),
]