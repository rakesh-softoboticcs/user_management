from django.forms import ModelForm
from .models import Users


class UserForm(ModelForm):
    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'user_name',
                  'email', 'password', 'confirm_password']
