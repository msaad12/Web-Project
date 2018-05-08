from django.conf.urls import url

from web_travel.views import AttractionView, HotelView, ResturantView, SearchView, ResturantReviewView, \
    ResturantDetailView, AttractionDetailsView, Travel_InformationView, HotelDetailsViews

urlpatterns = [
    url(r"^attractions/$", AttractionView.as_view(), name='attractions'),
    url(r"^hotels/$", HotelView.as_view(), name='hotels'),
    url(r"^detail/resturant/(?P<pk>\d+)/$", ResturantDetailView.as_view(), name='resturant_detail'),
    url(r"^resturants/$", ResturantView.as_view(), name='resturants'),
    url(r"^feedback/resturant/(?P<pk>\d+)/$", ResturantReviewView.as_view(), name='resturant_feedback'),
    url(r"^searches/$", SearchView.as_view(), name='searches'),
    url(r"^detail/attraction/(?P<pk>\d+)/$", AttractionDetailsView.as_view(), name='attraction_details'),
    url(r"^travel_info/$", Travel_InformationView.as_view(), name='travel_information'),
    url(r"^detail/hotel/(?P<pk>\d+)/$", HotelDetailsViews.as_view(), name='hotel_details'),

]