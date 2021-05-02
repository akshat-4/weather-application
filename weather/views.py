from django.shortcuts import render
import requests
def home(request):
    city = request.GET.get('searched-city', 'delhi')
    if city == "":
        city = 'delhi'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=b49a0e30781e0a81a866402649cb304e'
    data = requests.get(url).json()
    try:
        condition = data['weather'][0]['main']
        if condition == "Rain":
            weather1 = "images/Rain.gif"
        elif condition == "Dust":
            weather1 = 'images/Dust.gif'
        elif condition == "Clouds":
            weather1 = "images/Clouds.gif"
        elif condition == "Clear":
            weather1 = "images/Clear.gif"
        elif condition == "Haze":
            weather1 = "images/Haze.gif"
        else:
            weather1 = "images/Clear.gif"
        payload = {
            'city': data['name'],
            'ktemp': int(data['main']['temp']),
            'ctemp': int(data['main']['temp']-273),
            'pressure': data['main']['pressure'],
            'weather': data['weather'][0]['main'],
            'icon': weather1,
            'humidity': data['main']['humidity'],
            'wind': data['wind']['speed'],
        }
        context = {'data': payload, 'icon': weather1}
        return render(request, 'home.html', context)

    except:
        weather1 = "images/Clear.gif"
        payload = {
            'city': "not found!!",
            'ktemp': " ",
            'ctemp': " ",
            'pressure': " ",
            'weather': " ",
            'icon': " ",
            'humidity': " ",
            'wind': " ",
        }
        context = {'data': payload, 'icon': weather1}
        return render(request, 'home.html', context)
