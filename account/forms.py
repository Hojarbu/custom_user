from django import forms

from . import models


class CreateCustomUserForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput())
    phone = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.TextInput())
    email = forms.CharField(widget=forms.TextInput())
    photo = forms.ImageField(widget=forms.FileInput(), required=False)


    class Meta:
        model = models.CustomUser
        fields = [
            'full_name',
            'phone',
            'email',
            'photo',
            'password'
        ]
