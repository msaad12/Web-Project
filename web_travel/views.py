from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from web_travel.models import Travel, Attractions, Hotel, Resturants


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
        attractions = Attractions.objects.all()
        context['attractions'] = attractions
        return context

    def page2(request):
        if request.method == 'GET':
            search_query = request.GET.get('myInput',None)
            return render(request,'./frontend/Search.html',request.GET)