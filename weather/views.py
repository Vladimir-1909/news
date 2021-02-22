import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm
from django.views.generic import DeleteView


def weather(request):
    appid = 'ce22b38389e2471e1e60f34faf3f1bac'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.order_by('-id')

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'id': city.id,
            'city': city.name,
            'temp': int(res["main"]["temp"]),
            'icon': res["weather"][0]["icon"]
        }

        all_cities.append(city_info)

    context = {
        'all_info': all_cities,
        'form': form,
        'news': cities
    }

    return render(request, 'weather/weather.html', context)


class CityDeleteView(DeleteView):
    model = City
    success_url = '/weather/'
    template_name = 'weather/sity_delete.html'