from django.conf.urls import url

from web_travel.views import AttractionView, HotelView, ResturantView, SearchView

urlpatterns = [
    url(r"^attractions/$", AttractionView.as_view(), name='attractions'),
    url(r"^hotels/$", HotelView.as_view(), name='hotels'),
    url(r"^resturants/$", ResturantView.as_view(), name='resturants'),
    url(r"^searches/$", SearchView.as_view(), name='searches'),

]