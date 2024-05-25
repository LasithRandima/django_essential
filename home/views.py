from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

#send http responses to endpoint
# def home(request):
#     return HttpResponse("Hello, Django!")

# render html template
def home(request):
    return render(request, 'home/welcome.html', {'today' : datetime.today()})
