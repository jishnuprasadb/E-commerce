from django.urls import path
from ecommerce_app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',views.home,name='home'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('add_category',views.add_category,name='add_category'),
    path('add_product',views.add_product,name='add_product'),
    path('show_product',views.show_product,name='show_product'),
    path('show_customer',views.show_customer,name='show_customer'),
    path('signup_page',views.signup_page,name='signup_page'),
    path('login_page',views.login_page,name='login_page'),
    path('men_page',views.men_page,name='men_page'),
    path('women_page',views.women_page,name='women_page'),
    path('kid_page',views.kid_page,name='kid_page'),
    path('signup',views.signup,name='signup'),
    path(' login_',views.login_,name='login_'),
    path('category_add',views.category_add,name='category_add'),
    path('product_add',views.product_add,name='product_add'),
    path('cart_page',views.cart_page,name='cart_page'),
    path('edit_profile',views.edit_profile,name='edit_profile'),
    path('view_profile',views.view_profile,name='view_profile'),
    path('edit',views.edit,name='edit'),
    path('log_out',views.log_out,name='log_out'),
    path('delete_product/<int:pk>',views.delete_product,name='delete_product'),
    path('add_cart/<int:pk>',views.add_cart,name='add_cart'),
    path('delete_cart/<int:pk>',views.delete_cart,name='delete_cart')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)