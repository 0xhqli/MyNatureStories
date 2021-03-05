from django.contrib.auth.forms import UserCreationForm
from django import forms
from staffapp.models import MyUser
from SitSpots.models import Tag, Zone

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

class tagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('type', 'name', 'scientific_name','description','diet','habitat','terrestrial_biome')
    def save(self, commit=True):
        # Save the provided password in hashed format
        print("*"*60)
        tag = super().save(commit=False)
        if commit:
            tag.save()
        return tag
    # type = forms.CharField(max_length=255)
    # name =  forms.CharField(max_length=255)
    # scientific_name = forms.CharField(min_length=7,widget=forms.Textarea)
    # description = forms.CharField(min_length=7,widget=forms.Textarea)
    # diet = forms.CharField(min_length=7,widget=forms.Textarea)
    # habitat = forms.CharField(min_length=7,widget=forms.Textarea)
    # terrestrial_biome = forms.CharField(min_length=7,widget=forms.Textarea)

class zoneForm(forms.ModelForm):
    class Meta:
        model = Zone
        fields = ('name')
    def save(self, commit=True):
        # Save the provided password in hashed format
        print("*"*60)
        zone = super().save(commit=False)
        if commit:
            zone.save()
        return zone