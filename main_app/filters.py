import django_filters

from .models import CoffeeBean

class CoffeeBeanFilter(django_filters.FilterSet):
    class Meta:
        model = CoffeeBean
        fields = ['variety']