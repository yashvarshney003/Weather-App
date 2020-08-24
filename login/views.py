from django.shortcuts import render
from django.contrib import messages
from .models import students2
from .models import students
from .serializers import studentsSerializer
#from rest_framework import APIView
from rest_framework import status
from rest_framework import viewsets
from django.http  import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
import requests


def cityweather(request):
 result = None
 if request.method == 'GET':
   city = request.GET['city']
   print (city)
   api_address='http://api.openweathermap.org/data/2.5/weather?appid=acd57eb705c23fe2fe0de21a55ed1b05&q='
   url=api_address+city
   json_data = requests.get(url).json()
   print(type(json_data))
   result = dict()
   result['temp'] = json_data['main']['temp']
      
  	 	
 return render(request, "login/home.html",{'result': result}) 


#messages.add_message(request, messages.INFO, 'Hello world.')
# Create your views here.

