from django.contrib.auth.forms import UserCreationForm
from django import forms
from staffapp.models import MyUser

# class RegisterForm(forms.ModelForm):
#     class Meta:
#         model = MyUser
#         fields = ('username', 'email','first_name','last_name','is_admin')
#     is_admin=forms.BooleanField(widget=forms.CheckboxInput,required=False)
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

# class RegisterForm(forms.Form):
#     username = forms.CharField(max_length=45)
#     first_name = forms.CharField(max_length=45)
#     last_name = forms.CharField(max_length=45)
#     email = forms.EmailField()
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
#     is_admin=

class loginForm(forms.Form):
    username = forms.CharField(max_length=45, required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)

class tagForm(forms.Form):
    type = forms.CharField(max_length=255)
    name =  forms.CharField(max_length=255)
    scientific_name = forms.CharField(min_length=7,widget=forms.Textarea)
    description = forms.CharField(min_length=7,widget=forms.Textarea)
    diet = forms.CharField(min_length=7,widget=forms.Textarea)
    habitat = forms.CharField(min_length=7,widget=forms.Textarea)
    terrestrial_biome = forms.CharField(min_length=7,widget=forms.Textarea)