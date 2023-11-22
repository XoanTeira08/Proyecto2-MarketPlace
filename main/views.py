from django.views import generic
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login,logout
from .forms import CreateUserForm, LoginForm
from categorias.models import Categoria
from .models import CustomerSupport
from products.models import Product, CartItem, Cart
from django.http import JsonResponse
import json

# Create your views here.
def home(request):
    category = Categoria.objects.all()
    return render(request, 'main/home.html', {'category':category})

def loginPage(request):
    error = None

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
                error = 'Usuario o contraseña incorrecta'
        context={'error':error}
        return render(request, 'main/registration/login.html',context)
    

def logoutUser(request):
    logout(request)
    return redirect("main:login")

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

class CustomerSupportView(generic.CreateView):
    model = CustomerSupport
    fields = ['name', 'phone','email', 'message']
    template_name = 'main/customersupport.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def ShoppingCart (request):
    context = {}
    return render(request, 'cart.html',context)

def AddToCart (request):
    data=json.loads(request.body)
    product_id= data["id"]
    product= Product.objects.get(id=product_id)

    if request.user.is_authenticated:
        cart, created= Cart.objects.get_or_create(user=request.user, completed=False)
        cartitem, created= CartItem.objects.get_or_create(cart=cart, product=product)
        cartitem.quantity +=1
        cartitem.save()
        print(cartitem)
        
    return JsonResponse("Funciona", safe=False)