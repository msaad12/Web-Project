from django.contrib import admin

# Register your models here.
from web_travel.models import Hotel, Attractions, Travel, Resturants

admin.site.register(Hotel)
admin.site.register(Attractions)
admin.site.register(Travel)
admin.site.register(Resturants)
