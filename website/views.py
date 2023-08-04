from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Customer

def home(request):
    customers = Customer.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are logged in')
            return redirect('home')
        else:
            messages.success(request, 'There was an error logging in. Please try again')
            return redirect('home')
    else:
        return render(request, 'home.html', {'customers': customers})

# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have successfully registered!')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})

def customer_item(request, id):
    if request.user.is_authenticated:
        customer_item = Customer.objects.get(id=id)
        return render(request, 'customer.html', {'customer_item': customer_item})
    else:
        messages.success(request, 'You must be logged in to view customer information')
        return redirect('home')
