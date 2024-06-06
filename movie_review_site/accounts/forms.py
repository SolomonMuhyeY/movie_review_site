from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    profile = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'custom-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'profile')

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2', 'email']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update({
                'class': 'form-input mt-1 block w-full md:w-64 rounded-md shadow-sm border-lime-300 focus:border-red-300 focus:ring focus:ring-red-200 focus:ring-opacity-50 bg-gray-800 text-gray-100'
            })

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        if commit:
            user.save()
            user_profile = UserProfile(user=user)
            if self.cleaned_data['profile']:
                user_profile.image = self.cleaned_data['profile']
            user_profile.save()
        return user


