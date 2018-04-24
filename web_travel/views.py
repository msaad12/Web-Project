from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import TemplateView, DetailView, FormView

from web_travel.forms import ResturantReviewForm
from web_travel.models import Travel, Attractions, Hotel, Resturants, Country, ResturantFeedback, Air_transport, \
    Road_transport


class HomeView(TemplateView):
    template_name = 'frontend/travel.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        hotels = Travel.objects.all()

        context['places'] = hotels
        return context


class AttractionView(TemplateView):
    template_name = 'frontend/Attractions.html'
    def get_context_data(self, **kwargs):
        context = super(AttractionView, self).get_context_data(**kwargs)
        attractions = Attractions.objects.all()
        context['attractions'] = attractions
        return context


class HotelView(TemplateView):
    template_name = 'frontend/hotel.html'

    def get_context_data(self, **kwargs):
        context = super(HotelView, self).get_context_data(**kwargs)
        hotel = Hotel.objects.all()
        context['hotels'] = hotel
        return context


class ResturantView(TemplateView):
    template_name = 'frontend/resturant.html'

    def get_context_data(self, **kwargs):

        context = super(ResturantView, self).get_context_data(**kwargs)
        resturants = Resturants.objects.all()
        context['resturant'] = resturants
        return context

class SearchView(TemplateView):
    template_name = 'frontend/Search.html'

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        search = self.request.GET.get('myInput')
        country = Country.objects.get(country_name=search)
        hotels = Hotel.objects.filter(country_id=country.id)
        attractions = Attractions.objects.filter(country_id=country.id)
        resturants = Resturants.objects.filter(country_id=country.id)
        context['country'] = country
        context['hotels'] = hotels
        context['attractions'] = attractions
        context['resturants'] = resturants
        return context

class CountryView(TemplateView):
    template_name = 'frontend/Search.html'

    def get_context_data(self, **kwargs):

        context = super(CountryView, self).get_context_data(**kwargs)
        countries = Country.objects.all()
        context['country'] = countries
        return context

class ResturantDetailView(TemplateView):
    template_name = 'frontend/Resturant_reviews.html'

    def get_context_data(self, **kwargs):
        context = super(ResturantDetailView, self).get_context_data(**kwargs)
        context['rest'] = Resturants.objects.get(id=kwargs.get('pk'))
        context['form'] = ResturantReviewForm()
        context['rest_rating'] = ResturantFeedback.objects.filter(resturant_id=kwargs.get('pk'))
        return context

class ResturantReviewView(FormView):

    form_class = ResturantReviewForm
    
    def form_valid(self, form):
        try:
            ResturantFeedback.objects.create(
                resturant_id= self.kwargs.get('pk'),
                user=self.request.user,
                review=form.cleaned_data.get('review'),
                rating=form.cleaned_data.get('rating'),

            )
            return self.get_success_url()
        except Exception as ex:
            raise Exception (ex.__str__())

    def get_success_url(self):
        url = 'http://localhost:8000/web-travel/detail/resturant/' + self.kwargs.get('pk') + '/'
        return redirect(url)

class AttractionDetailsView(TemplateView):
    template_name = 'frontend/Attraction_Details.html'

    def get_context_data(self, **kwargs):
        context = super(AttractionDetailsView, self).get_context_data(**kwargs)
        context['attract'] = Attractions.objects.get(id=kwargs.get('pk'))
        return context

class Travel_InformationView(TemplateView):
    template_name = 'frontend/Travel_Information.html'

    def get_context_data(self, **kwargs):
        context = super(Travel_InformationView, self).get_context_data(**kwargs)
        context['air_travel'] = Air_transport.objects.all()
        context['road_transport'] = Road_transport.objects.all()
        return context