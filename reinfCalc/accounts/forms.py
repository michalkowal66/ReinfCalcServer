from django.contrib.auth.forms import UserCreationForm
from accounts.models import User


class UserSignUpForm(UserCreationForm):
    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = User
