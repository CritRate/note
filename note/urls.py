from django.urls import path
from django.views.generic import TemplateView, RedirectView
from django.urls import reverse

from .views import CreateNote, UpdateNote, DeleteNote, ListViewNote

app_name = 'note'

urlpatterns = [
    path('', TemplateView.as_view(template_name='note/home.html'), name='home'),
    path('notes', ListViewNote.as_view(), name='list_view' ),
    path('new/note', CreateNote.as_view(), name='create_note'),
    path('delete/note/<pk>', DeleteNote.as_view(), name='delete_note'),
    path('update/note/<pk>', UpdateNote.as_view(), name='update_note'),
]