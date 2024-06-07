from django.forms import ModelForm,Textarea
from .models import Review
from django import forms
from .models import Vote

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['review_text']
        widgets = {
            'review_text': Textarea(attrs={
                'rows': 2,
                'class': 'form-input mt-1 block w-full md:w-64 rounded-md shadow-sm border-lime-300 focus:border-red-300 focus:ring focus:ring-red-200 focus:ring-opacity-50 bg-gray-800 text-gray-100'
            })
        }

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ['vote_type']
