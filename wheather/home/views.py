from django.shortcuts import render, HttpResponse
import requests


# Create your views here.
def home(request):

    city = request.GET.get('city','goa')
   # city="goa"
    url = f'openweatherapilink={city}&appid=your api key link'
    data = requests.get(url).json()

    display_data = {
        'city':data['name'],
        'weather': data['weather'][0]['main'],
        'icon': data ['weather'][0]['icon'],
        'kelvin_temperature': data ['main']['temp'],
        'celcius_temperature': int(data ['main']['temp'] - 273 ),
        'pressure': data['main']['pressure'],
        'humidity': data['main']['humidity'],
        'description': data['weather'][0]['description']
       
    }
    context = {'data': display_data}
   # print(context)

    return render(request,'home.html', context)
#a
#b


    
