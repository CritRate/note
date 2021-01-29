from .models import Note

def my_notes(request):
    my_notes = Note.objects.filter(user=request.user).all()
    return {'my_notes': my_notes} 