from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=254)
    phone_number = forms.IntegerField()

    class Meta:
        model = User
        fields = ("name", "username", "email","phone_number", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.name = self.cleaned_data['name']
        user.phone_number = self.cleaned_data['phone_number']
        if commit:
            user.save()
        return user
