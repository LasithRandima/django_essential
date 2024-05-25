from django.urls import path
from . import views

urlpatterns = [
    # path('notes', views.list),
    path('notes', views.NotesListView.as_view()), # class based view
    # path('notes/<int:pk>', views.detail),
    path('notes/<int:pk>', views.NotesDetailView.as_view()), # class based view
]
