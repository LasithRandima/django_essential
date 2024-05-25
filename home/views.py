from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.

#send http responses to endpoint
# def home(request):
#     return HttpResponse("Hello, Django!")

# render html template
def home(request):
    return render(request, 'home/welcome.html', {'today' : datetime.today()})

# protected view. login required
@login_required(login_url='/admin')
def authorized(request):
    return render(request, 'home/authorized.html', {})
