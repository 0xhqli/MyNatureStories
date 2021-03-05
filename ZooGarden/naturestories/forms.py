from SitSpots.models import Post, Zone
from django import forms

class PostForm(forms.ModelForm):
    # author = forms.CharField(max_length=255, required=True)
    # title =  forms.CharField(max_length=255, required=True)
    # sitspot = forms.CharField(max_length=255, required=True)
    # content = forms.CharField(min_length=7,widget=forms.Textarea, required=True)
    # website = forms.URLField(required=False)
    # image = forms.ImageField(required=False, upload_to="static/naturestories/img")
    # zone = forms.ModelChoiceField(queryset= Zone.objects.all())
    class Meta: 
        model = Post
        fields = ('title','author','sitspot','zone','image','content', 'website', )