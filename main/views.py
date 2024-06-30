from django.shortcuts import render
import requests
from django.http import JsonResponse, HttpResponse
from .models import Condition


def welcome(request):
    url = 'https://api.weatherapi.com/v1/current.json?key=93e7b2612c5d436897652816243006&q='

    if request.method == 'POST':
        city = request.POST.get('city')
    else:
        city = 'Toshkent'
    data = requests.get(url+city)
    if data.status_code == 400:
        context = {
            'status_code': 400,
            'data': data.json()
        }
        return render(request, 'main/welcome.html', context)
    code = data.json()['current']['condition']['code']
    condition = Condition.objects.get(code=code)
    context = {
        'data': data.json(),
        'condition': condition,
        'city': city,
    }
    return render(request, 'main/welcome.html', context)
    # return JsonResponse(data.json()['location'])


def condition_add(request):
    data = requests.get('https://www.weatherapi.com/docs/weather_conditions.json')
    print(data.json())
    # for dat in data.json():
    #     condition = Condition.objects.create(
    #         code=dat['code'],
    #         text=dat['day']
    #     )
    #     condition.save()
    return HttpResponse(data)


def search_city(request):
    name = request.GET.get('q')
    url = 'https://api.weatherapi.com/v1/search.json?key=93e7b2612c5d436897652816243006&q='
    data = requests.get(url + str(name))
    context = {
        'data': data.json(),
    }
    return render(request, 'main/city.html', context)
