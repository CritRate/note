from django.urls import path, include

from .views import SignUpFormView

app_name = 'accounts'

urlpatterns = [
    path('', include('django.contrib.auth.urls'), name='authentication'),
    path('sign_up/', SignUpFormView.as_view(), name='sign_up'),
]
