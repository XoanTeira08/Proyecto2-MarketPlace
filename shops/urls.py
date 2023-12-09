from django.urls import path
from . import views

app_name="shops"

urlpatterns = [
    #path('', views.ShopListView.as_view(), name="shopList"),
    path('crearTienda/', views.ShopCreateView.as_view(), name="shopCreate"),
    path('<slug:slug>/', views.ShopDetailView.as_view(), name="shopDetail"),
    path('crearResena/<str:nombre_tienda>/', views.reviewShopCreateView.as_view(), name="reviewShopCreate"),
    #path('actualizarTienda/<slug:slug>/', views.ShopUpdateView.as_view(), name="shopUpdate"),
    #path('eliminarTienda/<slug:slug>/', views.ShopDeleteView.as_view(), name="shopDelete"),
]