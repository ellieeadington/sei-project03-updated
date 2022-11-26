from django import views
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cafes/', views.cafes_index, name='index'),

    # ROB SECTION
    path('cafes/<int:cafe_id>/', views.cafes_detail, name='detail'),
    
    # Delete and Update for Cafes
    path('cafes/<int:pk>/update/', views.CafeUpdate.as_view(), name='cafes_update'),
    path('cafes/<int:pk>/delete/', views.CafeDelete.as_view(), name='cafes_delete'),
    
    path('cafes/<int:cafe_id>/add_brewing_method/', views.add_brewing_method, name='add_brewing_method'),
    path('profile/cafe/<int:cafe_id>/brewing_methods/update', views.brewing_method_edit, name='brewing_method_edit'),

    path('cafes/<int:cafe_id>/add_event/', views.add_event, name='add_event'),
    path('profile/cafe/<int:cafe_id>/events/', views.event_edit, name='event_edit'),

    # ASHISH SECTIO
    # path('profile/update/', views.has_profile_submitted, name='has_profile_submitted'),
    
    path('accounts/password/reset',  
     auth_views.PasswordResetView.as_view(
             template_name='registration/password_reset.html'
             ),
        name='password_reset'
    ),

    path('accounts/password/reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='registration/password_reset_done.html'
         ),
        name= 'password_reset_done'
    ),
    path('accounts/password/reset/confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/password_reset_confirm.html'
         ),
        name = 'password_reset_confirm'
    ),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password_reset_complete.html'
         ),
    name='password_reset_complete'),

    # ELLIE SECTION
    path('coffee_beans/', views.coffee_beans_index, name='coffee_beans_index'),
    path('coffee_beans/<int:coffee_beans_id>/', views.coffee_beans_detail, name='coffee_beans_detail'),

    path('signup/', views.signup, name="signup"),
    path('signup/register-cafe/', views.register_cafe, name="register_cafe"),
    path('signup/register-cafe/new-cafe', views.cafe_form, name="cafe_form"),
    path('profile/', views.profile, name='profile'),
    path('user/update/<int:pk>/', views.UserUpdate.as_view(), name='user_update'),
    
    path('profile/cafe/<int:cafe_id>/coffee_beans/', views.coffee_bean_edit, name='coffee_bean_edit'),
    path('profile/cafe/<int:cafe_id>/coffee_beans/add_coffee_bean/', views.add_coffee_bean, name='add_coffee_bean'),
    path('profile/cafe/<int:pk>/coffee_beans/update/', views.CoffeeBeanUpdate.as_view(), name='coffee_bean_update'),
    path('profile/cafe/<int:pk>/coffee_beans/delete/', views.CoffeeBeanDelete.as_view(), name='coffee_bean_delete'),
    
    path('cafes/<int:cafe_id>/add_review/', views.add_review, name='add_review'),
    
    path('search/', views.search, name="search"),

    path('profile/cafe/<int:pk>/brewing_methods/delete/', views.BrewingMethodDelete.as_view(), name='brewing_method_delete'),
    
    
]
