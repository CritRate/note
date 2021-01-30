from django.forms import ModelForm

from .models import Note

class NoteForm(ModelForm):
    model = Note
    class Meta:
        include = ('title', 'content')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'note-title'
        self.fields['content'].widget.attrs['class'] = 'note-content'