from asyncio.windows_events import NULL
from itertools import product
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from ecommerce_app.models import Customer,Category,Products,Cart
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    product=Products.objects.all()
    return render(request,'home.html',{'product':product})

@login_required(login_url='login_page')
def admin_home(request):
    return render(request,'admin_home.html')  

@login_required(login_url='login_page')
def add_category(request):
    return render(request,'add_category.html')   

@login_required(login_url='login_page')
def add_product(request):
    cat=Category.objects.all()
    return render(request,'add_product.html',{'cat':cat})

@login_required(login_url='login_page')
def show_product(request):
    product=Products.objects.all()
    return render(request,'show_product.html',{'product':product})
    
@login_required(login_url='login_page')    
def show_customer(request):
    customer=Customer.objects.all()
    return render(request,'show_customer.html',{'customer':customer})   
    
def signup_page(request):
    return render(request,'signup.html')   

def login_page(request):
    return render(request,'login.html')     

def men_page(request):
    cats=Category.objects.get(category='mens shirt')
    men_shirt=Products.objects.filter(category=cats)
    catj=Category.objects.get(category='mens jeans')
    men_jean=Products.objects.filter(category=catj)
    catf=Category.objects.get(category='mens footwear')
    men_fw=Products.objects.filter(category=catf)
    return render(request,'men.html',{'men_shirt':men_shirt,'men_jean':men_jean,'men_fw':men_fw})

def women_page(request):
    cats=Category.objects.get(category='womens saree')
    women_saree=Products.objects.filter(category=cats)
    catk=Category.objects.get(category='womens skirts')
    women_skirt=Products.objects.filter(category=catk)
    catf=Category.objects.get(category='womens fashion')
    women_fsn=Products.objects.filter(category=catf)
    return render(request,'women.html',{'women_saree':women_saree,'women_skirt':women_skirt,'women_fsn': women_fsn})    

def kid_page(request):
    cats=Category.objects.get(category='kids Tshirt')
    kids_tshrts=Products.objects.filter(category=cats)
    catr=Category.objects.get(category='kids trousers')
    kids_trosr=Products.objects.filter(category=catr)
    catt=Category.objects.get(category='kids toys')
    kids_toy=Products.objects.filter(category=catt)
    return render(request,'kid_page.html',{'kids_tshrts': kids_tshrts,'kids_trosr':kids_trosr,'kids_toy':kids_toy})    

def signup(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        email=request.POST['email']
        if password==cpassword: 
            if User.objects.filter(username=username).exists(): 
                messages.info(request, 'This username already exists!!!!!!')
                return redirect('signup_page')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password,
                    email=email)
                user.save()
                phone_number=request.POST['ph_no']
                address=request.POST['adrs']
                data=User.objects.get(id=user.id)
                user=Customer(customer=data,phone_number=phone_number,address=address)
                user.save()
                print("Successed...")
                return redirect('login_page')
        else:
            messages.info(request, 'Password doesnt match!!!!!!!')
            print("Password is not Matching.. ") 
            return redirect('signup_page')   
        

def login_(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('admin_home')
            else:
                login(request,user)
                auth.login(request,user) 
                return redirect('login_home')   
        
   
def category_add(request):
    if request.method=='POST':
        cat=request.POST['cat1']
        category=Category(category=cat)
        category.save()
        return redirect('admin_home')



def product_add(request):
    if request.method=='POST':
        cat=request.POST['select']       
        image=request.FILES.get('file') 
        brand=request.POST['brand']
        price=request.POST['price']
        data=Category.objects.get(id=cat)
        product=Products(category=data,image=image,brand=brand,price=price)
        product.save()
        return redirect('admin_home')

@login_required(login_url='login_page')
def login_home(request):
    product=Products.objects.all()
    return render(request,'login_home.html',{'product':product})

@login_required(login_url='login_page')
def cart_page(request):
    cart=Cart.objects.filter(user=request.user)
    return render(request,'cart.html',{'cart':cart})   

def add_cart(request,pk):
    products=Products.objects.get(id=pk)
    data=Cart(product=products,user=request.user)
    data.save()
    return redirect('cart_page')       

@login_required(login_url='login_page')
def view_profile(request):
    customer=Customer.objects.get( customer=request.user)
    return render(request,'view_profile.html',{'customer':customer})

@login_required(login_url='login_page')
def edit_profile(request):
    customer=Customer.objects.get( customer=request.user)
    return render(request,'editpage.html',{'customer':customer})

def edit(request):
    if request.method=='POST':
        customer=Customer.objects.get(customer=request.user)
        customer.customer.first_name=request.POST.get('first_name')
        customer.customer.last_name=request.POST.get('last_name')
        customer.customer.email=request.POST.get('email')
        customer.phone_number=request.POST.get('ph_no')
        customer.address=request.POST.get('adrs')
        customer.save()
        return redirect('view_profile')

@login_required(login_url='login_page')
def log_out(request):
    auth.logout(request)
    return redirect('home')

def delete_product(request,pk):
    product=Products.objects.get(id=pk)
    product.delete()
    return redirect('show_product')

def delete_cart(request,pk):
    cart=Cart.objects.get(id=pk) 
    cart.delete()
    return redirect('cart_page')   


