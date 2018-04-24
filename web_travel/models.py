from django.conf import settings
from django.db import models

# Create your models here.
class Hotel(models.Model):
    hotel_name = models.CharField(max_length=30)
    hotel_image = models.ImageField(upload_to=u'hotel_image/%Y/%m/%d')
    hotel_image1 = models.ImageField(upload_to=u'hotel_image1/%Y/%m/%d', null=True, blank=True)
    hotel_image2 = models.ImageField(upload_to=u'hotel_image2/%Y/%m/%d', null=True, blank=True)
    hotel_rating = models.IntegerField()
    country = models.ForeignKey('Country', related_name='hotel_country', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hotel_name

class Attractions(models.Model):
    attraction_name = models.CharField(max_length=30)
    attraction_image = models.ImageField(upload_to=u'attraction_image/%Y/%m/%d')
    attraction_image1 = models.ImageField(upload_to=u'attraction_image1/%Y/%m/%d', null=True, blank=True)
    attraction_image2 = models.ImageField(upload_to=u'attraction_image2/%Y/%m/%d', null=True, blank=True)
    attraction_rating = models.IntegerField()
    country = models.ForeignKey('Country', related_name='attractions_country', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.attraction_name


class Travel(models.Model):
    travel_name = models.CharField(max_length=30)
    travel_image = models.ImageField(upload_to=u'travel_image/%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.travel_name

class Resturants(models.Model):
    resturant_name = models.CharField(max_length=30)
    resturant_image = models.ImageField(upload_to=u'resturant_image/%Y/%m/%d')
    image1 = models.ImageField(upload_to=u'resturant_image1/%Y/%m/%d', null=True, blank=True)
    image2 = models.ImageField(upload_to=u'resturant_image2/%Y/%m/%d', null= True, blank=True)
    country = models.ForeignKey('Country', related_name='resturants_country', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.resturant_name


class Country(models.Model):

    country_name = models.CharField(max_length=30)
    intro = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.country_name


class ResturantFeedback(models.Model):

    resturant = models.ForeignKey('Resturants', related_name='resturant_rating')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_resturant_rating')
    review = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.resturant.resturant_name

class Air_transport(models.Model):

    aeroplane_name = models.CharField(max_length=20)
    aeroplane_image = models.ImageField(upload_to=u'aeroplane_image/%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.aeroplane_name


class Road_transport(models.Model):
    bus_name = models.CharField(max_length=20)
    bus_image = models.ImageField(upload_to=u'bus_image/%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.bus_name

