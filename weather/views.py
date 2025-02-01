from django.shortcuts import render
import requests
import datetime
from dotenv import dotenv_values

config = dotenv_values(".env")  # Load .env file manually
API_KEY = config.get("API_KEY")

# Create your views here.

def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'kathmandu'
    
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    PARAMS={'units':'metric'}

    response=requests.get(url,params=PARAMS)

    if response.status_code==200:
        data=response.json()
        description=data['weather'][0]['description']
        icon=data['weather'][0]['icon']
        temp=data['main']['temp']
    
    else:
        description = 'Unable to fetch weather data'
        icon = ''
        temp = 'N/A'

    day=datetime.date.today()

    return render(request,'index.html',{
        'description':description,
        'icon':icon,
        'temp':temp,
        'day':day,
         'city': city
    })
import os
from dotenv import load_dotenv

load_dotenv()  # Explicitly load .env file

API_KEY = os.getenv('API_KEY')
print(f"API Key in views.py: {API_KEY}")  # Debugging line

