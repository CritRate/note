from django.urls import path
from django.views.generic import TemplateView, RedirectView
from django.urls import reverse

from .views import NoteCreateView, NoteDeleteView, NoteDetailView, NoteUpdateView, ListViewNote, HomeView

app_name = 'note'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('list/', ListViewNote.as_view(), name='list_view' ),
    path('new/', NoteCreateView.as_view(), name='create_note'),
    path('delete/<pk>/', NoteDeleteView.as_view(), name='delete_note'),
    path('update/<pk>/', NoteUpdateView.as_view(), name='update_note'),
    path('<pk>/', NoteDetailView.as_view(), name='detail_note'),
]