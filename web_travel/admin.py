from django.contrib import admin

# Register your models here.
from web_travel.models import Hotel, Attractions, Travel, Resturants, Country, ResturantFeedback, Road_transport, \
    Air_transport

admin.site.register(Hotel)
admin.site.register(Attractions)
admin.site.register(Travel)
admin.site.register(Resturants)
admin.site.register(Country)
admin.site.register(ResturantFeedback)
admin.site.register(Air_transport)
admin.site.register(Road_transport)