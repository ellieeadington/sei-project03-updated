from django.forms import ModelForm
from .models import BrewingMethod, CoffeeBean, Event, Review

class BrewingMethodForm(ModelForm):
    class Meta:
        model = BrewingMethod
        fields = ['method_name', 'method_bio']

        
class CoffeeBeanForm(ModelForm):
    class Meta:
        model = CoffeeBean
        fields = ['name', 'variety', 'description', 'roastery', 'date_harvested', 'image', 'location']        

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'event_description', 'event_type', 'event_date', 'event_time_from', 'event_time_to']

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['review_title', 'review_body', 'stars']
        
        