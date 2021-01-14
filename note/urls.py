from django.urls import path
from django.views.generic import TemplateView, RedirectView
from django.urls import reverse

name = 'note'

urlpatterns = [
    path('', RedirectView.as_view(url=reverse('note:home'))),
    path('note', TemplateView.as_view(template_name='note/home.html'), name='home')
]