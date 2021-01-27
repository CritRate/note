from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.forms import EmailField

User = get_user_model()


class SignUpForm(UserCreationForm):
    email = EmailField(max_length=255, help_text='Valid email address')

    def send_success_email(self):
        with open('log.txt', 'w') as file:
            file.write('Sign Up Sucessfull')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')