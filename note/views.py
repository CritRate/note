from typing import List
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
from .models import Note

class CreateNote(CreateView):
    model = Note
    fields = ['title', 'content']
    success_url = reverse_lazy('note:list_view')


class UpdateNote(UpdateView):
    model = Note
    fields = ['title', 'content']
    success_url = reverse_lazy('note:list_view')

class DeleteNote(DeleteView):
    model = Note
    success_url = reverse_lazy('note:list_view')


class ListViewNote(ListView):
    model = Note
    paginate_by = 10
