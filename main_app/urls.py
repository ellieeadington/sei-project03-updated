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
    # Delete and Update for Cafes
    path('cafes/<int:pk>/update/', views.CafeUpdate.as_view(), name='cafes_update'),
    path('cafes/<int:pk>/delete/', views.CafeDelete.as_view(), name='cafes_delete'),
    
    path('cafes/<int:cafe_id>/add_brewing_method/', views.add_brewing_method, name='add_brewing_method'),
    
    
    
    
    
    
    # ASHISH SECTION
    path('acounts/signup', views.signup, name="signup"),
    
    
    
    
    
    
    

    # ELLIE SECTION
    path('coffee_beans/', views.coffee_beans_index,name='coffee_beans_index'),
    path('coffee_beans/<int:coffee_beans_id>', views.coffee_beans_detail, name='coffee_beans_detail'),
    


    
    
    
]