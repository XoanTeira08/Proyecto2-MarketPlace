from django.urls import path
from . import views

app_name="main"

urlpatterns = [
    path('', views.home, name="home"),
    path('login/',views.loginPage, name="login"),
    path('logout/',views.logoutUser, name="logout"),
    path('register/',views.registerPage, name="register"),
    path("ShoppingCart/",views.ShoppingCart, name="Cart"),
    path('customersupport/',views.CustomerSupportView.as_view(), name="customerSupport"),
    path("AddToCart",views.AddToCart, name="Add"),
]