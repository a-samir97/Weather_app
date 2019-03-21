from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
# Create your views here.

def index (request):
    #a77afcb406c2ed79cf57d132bb86fba9
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=a77afcb406c2ed79cf57d132bb86fba9'
    cities = City.objects.all()
    weather_data = []

    if  request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    
    form = CityForm()

    for city in cities:

        r = requests.get(url.format(city)).json()
        city_weather = {
            'city':city,
            'temperature':r['main']['temp'],
            'description':r['weather'][0]['description'],
            'icon':r['weather'][0]['icon']
        }
        weather_data.append(city_weather)

    context = {'weather_data':weather_data,'form':form}

    return render(request,"weather.html",context)