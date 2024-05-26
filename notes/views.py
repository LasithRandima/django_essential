from django.shortcuts import render
from .models import Notes
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.

class NotesCreateView(CreateView):
    model = Notes
    fields = ['title', 'content']
    success_url = '/smart/notes'
    template_name = 'notes/notes_form.html'

class NotesListView(ListView):
    model = Notes
    # template_name = 'notes/notes_list.html'   # default template name is notes/notes_list.html. so we don't need to specify it beacuse we follow the naming convention
    context_object_name = 'notes'
    paginate_by = 10

# def list(request):
#     notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': notes})


class NotesDetailView(DetailView):
    model = Notes
    # template_name = 'notes/notes_detail.html'   # default template name is notes/notes_detail.html. so we don't need to specify it beacuse we follow the naming convention
    context_object_name = 'note'

# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404('Note does not exist')
#     return render(request, 'notes/notes_detail.html', {'note': note})