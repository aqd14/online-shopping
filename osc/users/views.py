from django.http.response import HttpResponse, Http404
from django.shortcuts import render, redirect

from users.models import Customer
from users.forms import RegistrationForm, LoginForm


# Create your views here.
def register(request):
    """Register new user
    """
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print('Valid form')
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password_confirm = form.cleaned_data['password_confirm']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            
            # check if username or email already exists in database
            exist = True if Customer.objects.filter(email=email, username=username).count() > 0 else False 
            if exist:
                # Display error to user
                print('Customer already created!')
            else:
                # Create new Customer instance and insert to database
                customer = Customer(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
                customer.save()
        else:
            print(form.errors)
    else:
        form = RegistrationForm()
        return render(request, 'signup.html', {'form' : form})
    
def login(request):
    """Handle login request from user
    
    Parameters
    ----------
    request :  HTTP request
    
    Returns
    -------
    response : HTTP response
        + Redirect to Home page if login successfully
        + Redirect to Registration page if user click on [Register] button
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            if request.POST.get('register'):
                return redirect('/signup/')
            else: # User clicked login
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                
                users = Customer.objects.filter(email=email, password=password)
                if len(users) > 0:
                    return HttpResponse('Login successfully!')
                else:
                    return HttpResponse('Login failed!')
        else:
            return HttpResponse('Form is invalid!')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form' : form})