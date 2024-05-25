from django.urls import path
# import views from home app
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('authorized', views.authorized),
]