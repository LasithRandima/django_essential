from django.urls import path
# import views from home app
from . import views

urlpatterns = [
    # path('home', views.home, name='home'), # function based view
    path('home', views.HomeView.as_view(), name='home'), # class based view
    path('authorized', views.AuthorizedView.as_view()), # class based view
]