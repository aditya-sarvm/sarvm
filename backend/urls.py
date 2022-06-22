from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('TopLanguages/', views.getTopLanguages, name="Languages"),
    path('TopStates/', views.getTopStates, name="States"),
    path('TopCities/', views.getTopCities, name="Cities"),
    path('Categories/', views.getCategories, name="Categories"),
    path('SubCategories/', views.getSubCategories, name="SubCategories"),
    path('MicroCategories/', views.getMicroCategories, name="MicroCategories"),
    path('Products/', views.getProducts, name="Products")
]
