from django.contrib.auth.forms import UserCreationForm
from account.models import CustomUserModel
from django import forms

class KayitFormu(UserCreationForm):
    class Meta:
        model=CustomUserModel
        fields=(
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2'
        )
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and not email.endswith('@ogr.cbu.edu.tr'):
            raise forms.ValidationError("Sadece @ogr.cbu.edu.tr uzantılı email adresleri kabul edilir.")
        return email
