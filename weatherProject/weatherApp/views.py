from django.shortcuts import render
from django.http import JsonResponse
import urllib.request
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def index(request):
    if (request.method == 'POST'):
        body = json.loads(request.body)
        city = body['city']
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +
                                        city+'&units=metric&appid=370191f3e6798c0d57cc54d7bcda569b').read()

        list_of_data = json.loads(source)

        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ', '
            + str(list_of_data['coord']['lat']),

            "temp": str(list_of_data['main']['temp']),
            "temp_min":  str(list_of_data['main']['temp_min']),
            "temp_max":  str(list_of_data['main']['temp_max']),
            "wind_speed": str(list_of_data['wind']['speed']),
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'],
        }
    else:
        data = {}
    return JsonResponse(data)
