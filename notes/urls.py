from django.urls import path
from . import views

urlpatterns = [
    # path('notes', views.list),
    path('notes', views.NotesListView.as_view(), name='notes_list'), # class based view
    # path('notes/<int:pk>', views.detail),
    path('notes/<int:pk>', views.NotesDetailView.as_view(), name="notes.detail"), # class based view
    path('notes/new', views.NotesCreateView.as_view(), name='notes.new'), # class based view
]
