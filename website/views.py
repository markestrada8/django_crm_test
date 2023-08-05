from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddCustomerForm
from .models import Customer

def home(request):
    customers = Customer.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are logged in.')
            return redirect('home')
        else:
            messages.success(request, 'There was an error logging in. Please try again.')
            return redirect('home')
    else:
        return render(request, 'home.html', {'customers': customers})

# USER CONTROLLERS

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
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

# CUSTOMER CONTROLLERS

def customer_item(request, id):
    if request.user.is_authenticated:
        customer_item = Customer.objects.get(id=id)
        return render(request, 'customer.html', {'customer_item': customer_item})
    else:
        messages.success(request, 'You must be logged in to perform that action.')
        return redirect('home')

def delete_customer(request, id):
    if request.user.is_authenticated:
        item_to_delete = Customer.objects.get(id=id)
        item_to_delete.delete()
        messages.success(request, 'Customer record deleted successfully')
        return redirect('home')
    else:
        messages.success(request, 'You must be logged in to perform that action.')
        return redirect('home')

def add_customer(request):
    form = AddCustomerForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_customer = form.save()
                messages.success(request, 'New customer saved')
                return redirect('home')
        return render(request, 'add_customer.html', {'form':form})
    else:
        messages.success(request, 'You must be logged in to perform that action.')
        return redirect('home')

def update_customer(request, id):
	if request.user.is_authenticated:
		current_customer = Customer.objects.get(id=id)
		form = AddCustomerForm(request.POST or None, instance=current_customer)
		if form.is_valid():
			form.save()
			messages.success(request, 'Information has been updated.')
			return redirect('home')
		return render(request, 'update_customer.html', {'form':form})
	else:
		messages.success(request, 'You must be logged in to perform that action.')
		return redirect('home')

