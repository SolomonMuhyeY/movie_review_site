from django.contrib.auth.forms import UserCreationForm
from django import forms
class UserCreateForm(UserCreationForm):
  email = forms.EmailField(required = True)
  def __init__(self,*args,**kwargs):
    super(UserCreationForm,self).__init__(*args, **kwargs)
    for fieldname in ['username', 'password1', 
 'password2','email']:
      self.fields[fieldname].help_text = None
      self.fields[fieldname].widget.attrs.update({
       'class': 'form-input mt-1 block w-full md:w-64 rounded-md shadow-sm border-lime-300 focus:border-red-300 focus:ring focus:ring-red-200 focus:ring-opacity-50 bg-gray-800 text-gray-100'
      })