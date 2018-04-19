from django.db import models

# Create your models here.
class Hotel(models.Model):
    hotel_name = models.CharField(max_length=30)
    hotel_image = models.ImageField(upload_to=u'hotel_image/%Y/%m/%d')
    hotel_rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hotel_name

class Attractions(models.Model):
    attraction_name = models.CharField(max_length=30)
    attraction_image = models.ImageField(upload_to=u'attraction_image/%Y/%m/%d')
    attraction_rating = models.IntegerField()
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
    resturant_rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.resturant_name


