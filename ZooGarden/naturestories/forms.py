from SitSpots.models import Post, Zone
from django import forms

class PostForm(forms.Form):
    author = forms.CharField(max_length=255, required=True)
    title =  forms.CharField(max_length=255, required=True)
    content = forms.CharField(min_length=7,widget=forms.Textarea, required=True)
    website = forms.URLField(required=False)
    image = forms.ImageField(required=False)
    zone = forms.ModelChoiceField(queryset= Zone.objects.all())