from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView # for class based views only
from django.contrib.auth.mixins import LoginRequiredMixin # for class based views only if login required use this mixin helpher class

# Create your views here.

#send http responses to endpoint
# def home(request):
#     return HttpResponse("Hello, Django!")

# render html template

# class based view for home page
class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today' : datetime.today()}
    


#  Function based view for home page
# def home(request):
#     return render(request, 'home/welcome.html', {'today' : datetime.today()})


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'
    
    
# protected view. login required
# @login_required(login_url='/admin')
# def authorized(request):
#     return render(request, 'home/authorized.html', {})
