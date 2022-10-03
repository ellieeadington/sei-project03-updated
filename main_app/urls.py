from django import views
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cafes/', views.cafes_index, name='index'),

    # ROB SECTION
    path('cafes/<int:cafe_id>', views.cafes_detail, name='detail'),
    path('cafes/create/', views.CafeCreate.as_view(), name='cafes_create'),
    
    
    
    
    
    
    
    # ASHISH SECTION
    
    
    
    
    
    
    
    # Ellie SECTION
    # path()
    
    
    
]