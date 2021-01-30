from .models import Note

def my_notes(request):
    my_notes = None
    if request.user.is_authenticated:
        my_notes = Note.objects.filter(user=request.user).all()
    return {'my_notes': my_notes} 