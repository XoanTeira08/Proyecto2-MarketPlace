from django.urls import path
from . import views

app_name="categorias"

urlpatterns = [
    path('', views.CategoriaListView.as_view(), name="categoryList"),
    path('<slug:slug>/', views.CategoriaDetailView.as_view(), name="categoryDetail"),
    path('crearCategoria/', views.CategoriaCreateView.as_view(), name="categoryCreate"),
    path('actualizarCategoria/<slug:slug>/', views.CategoriaUpdateView.as_view(), name="categoryUpdate"),
    path('eliminarCategoria/<slug:slug>/', views.CategoriaDeleteView.as_view(), name="categoryDelete"),
]