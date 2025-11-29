from django.shortcuts import render,redirect
from .models import Order
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

def home(request):
    return render(request,"base.html")

def menu(request):
    return render(request,"menu.html")

def order(request):
    if request.method == "POST":
        pizza_name = request.POST.get('pizza_name')
        pizza_type = request.POST.get('pizza_type')
        quantity = request.POST.get('quantity')
        customer_name = request.POST.get('customer_name')
        contact = request.POST.get('contact')
        address = request.POST.get('address')

        Order.objects.create(
            pizza_name=pizza_name,
            pizza_type=pizza_type,
            quantity=quantity,
            customer_name=customer_name,
            contact=contact,
            address=address
        )

        return redirect('services')
    return render(request, 'order.html')


def services(request):
    orders = Order.objects.all().order_by('-ordered_at')
    return render(request,"services.html", {'orders': orders})

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect('home') 
    return render(request,"signup.html")


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {username}!")
            return redirect('home')  
        else:
            messages.error(request, "Invalid username or password. Please try again.")

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    messages.success(request, "You have logged out successfully.")
    return redirect('home') 
    