from tkinter import CASCADE
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

STARS = (
    ('5', '★★★★★'),
    ('4', '★★★★'),
    ('3', '★★★'),
    ('2', '★★'),
    ('1', '★'),    
)

VARIETIES = (
    ('A', 'Arabica'),
    ('R', 'Robusta'),
    ('L', 'Liberica'),
    ('E', 'Excelsa')
)

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     is_cafe = models.BooleanField

class CoffeeBean(models.Model):
    name = models.CharField(max_length=250)
    variety =  models.CharField(max_length=1000, choices=VARIETIES, default=VARIETIES[0][0])
    description = models.CharField(max_length=2000)
    roastery = models.CharField(max_length=250)
    date_harvested = models.CharField(max_length=250)
    image = models.ImageField(upload_to ='main_app/static/uploads', default="no image uploaded")
    location = models.CharField(max_length=250)
    
# Create your models here.

class Cafe(models.Model):
    cafe_name = models.CharField(max_length=250, blank=True)
    cafe_bio = models.CharField(max_length=2500, blank=True)
    date_founded = models.DateField()
    address_line_1 = models.CharField(max_length=250, blank=True)
    address_line_2 = models.CharField(max_length=250, blank=True)
    address_city = models.CharField(max_length=250, blank=True)
    address_county = models.CharField(max_length=250, blank=True)
    address_country = models.CharField(max_length=250, blank=True)
    address_postcode = models.CharField(max_length=10, blank=True)
    cafe_image = models.ImageField(upload_to ='main_app/static/uploads', default="no image uploaded")
    menu_image = models.ImageField(upload_to ='main_app/static/uploads', default="no image uploaded")
    cafe_website = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coffee_beans = models.ManyToManyField(CoffeeBean, blank=True)
    
    def get_absolute_url(self):
        return reverse('detail', kwargs = {'cafe_id': self.id})
    
class Event(models.Model):

    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)   
    event_name = models.CharField(max_length=250)
    event_description = models.CharField(max_length=1000)
    event_weekday = models.CharField(max_length=20)
    event_time_from = models.TimeField()
    event_time_to = models.TimeField()
    event_image = models.CharField(max_length=1000)
    
class Review(models.Model):
    datetime = models.DateTimeField()
    stars = models.CharField(max_length=2, choices=STARS, default=STARS[0][0])
    review_title = models.CharField(max_length=250)
    review_body = models.CharField(max_length=1000)
    
class CafeOpening(models.Model):
    weekday_open = models.CharField(max_length=250)
    open_from = models.TimeField()
    open_from = models.TimeField()
    
class BrewingMethod(models.Model):
    brewing_method = models.CharField(max_length=250)
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
        
    
        

    
    
    
    