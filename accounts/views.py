from django.shortcuts import render
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate

from .forms import SignUpForm

# Create your views here.


class SignUpFormView(FormView):
    form_class = SignUpForm
    template_name = 'registration/sign_up.html'
    success_url = reverse_lazy('note:home')

    def form_valid(self, form ):
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(self.request, username=username, password=password)
        login(self.request, user)
        form.send_success_email()
        return super().form_valid(form)