import requests
from django.shortcuts import render

def index(request):
    api_key = 'a6ec7b3179cd03a68214baaff63da702'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + api_key

    city = 'Prague'
    response = requests.get(url.format(city)).json()

    city_info = {
        'city': city,
        'temp': response['main']['temp'],
        'icon': response['weather'][0]['icon'],
        'main': response['main']['humidity']
    }


    context = {'info': city_info}
    return render(request, 'weather/weather.html', context)

