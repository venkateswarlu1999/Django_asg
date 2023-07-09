from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from .models import Registration,studentsdata,Login
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout
from django .http import HttpResponse

def homepage(request):
    data_from_admin = studentsdata.objects.all()
    return render(request, 'homepage.html', {'data_from_admin': data_from_admin})

# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = RegistrationForm()
    
#     return render(request, 'register.html', {'form': form})
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Create a new user object using the submitted username and password
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, password=password)
            
            # Save the additional registration fields
            name = form.cleaned_data['name']
            mobile = form.cleaned_data['mobile']
            Registration.objects.create(name=name, mobile=mobile,username=username,password=password)
            
            # Save the login fields
            Login.objects.create(user=user)
            
            return redirect('login')
    else:
        form = RegistrationForm()
    
    return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if Registration.objects.filter(username=username, password=password).exists():
                return redirect('homepage')
            else:
                error_message = 'Invalid username or password'
                return render(request, 'login.html', {'form': form, 'error_message': error_message})
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})
def logout(request):
    auth_logout(request)
    return redirect('login')
