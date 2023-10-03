from django.shortcuts import render

from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login,logout
from .forms import CreateUserForm, LoginForm

# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def categories(request):
    return render(request, 'main/categories.html')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect("main:home")
    else:
        if request.method == 'POST':
            username= request.POST.get('username')
            password= request.POST.get('password')

            user= authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("main:home")
            else:
                messages.info(request, 'Username OR password is incorrect')
        context={}
        return render(request, 'main/registration/login.html',context)
    

def registerPage(request):
    if request.user.is_authenticated:
        return redirect("main:home")
    else:
        form= CreateUserForm()
        if request.method == 'POST':
            form= CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user =  form.cleaned_data.get('username')
                messages.success(request, 'Account was created for' + user)

                return redirect('main:login')
            
        context = {'form':form}
        return render(request, 'main/registration/register.html',context)
