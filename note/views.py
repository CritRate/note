from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView, View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from .models import Note

class HomeView(View):
    template_name = 'note/home.html'
    
    def get(self, request):
        return render(request, self.template_name)

class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'content']
    success_url = reverse_lazy('note:home')


    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super().form_valid(form)


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    fields = ['title', 'content']
    success_url = reverse_lazy('note:home')

    def get_queryset(self):
        query = super().get_queryset()
        return query.filter(user=self.request.user)
        

class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = reverse_lazy('note:home')


class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note


class ListViewNote(LoginRequiredMixin, ListView):
    model = Note
    paginate_by = 10
