from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import BrewingMethod, CoffeeBean, Cafe, Profile, Event, Review

admin.site.register(CoffeeBean)
admin.site.register(Cafe)
admin.site.register(BrewingMethod)
admin.site.register(Profile)
admin.site.register(Event)
admin.site.register(Review)
