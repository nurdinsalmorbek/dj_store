from django.shortcuts import render

def index(request):
    api_key = 'a6ec7b3179cd03a68214baaff63da702'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=' + api_key

    city = 'London'


    return render(request, 'weather/weather.html')

