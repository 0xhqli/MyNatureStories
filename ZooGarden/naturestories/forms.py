from SitSpots.models import Post, Zone, Comment, Reply, Tag
from django import forms

class PostForm(forms.ModelForm):
    # author = forms.CharField(max_length=255, required=True)
    # title =  forms.CharField(max_length=255, required=True)
    # sitspot = forms.CharField(max_length=255, required=True)
    # content = forms.CharField(min_length=7,widget=forms.Textarea, required=True)
    # website = forms.URLField(required=False)
    # image = forms.ImageField(required=False, upload_to="static/naturestories/img")
    # zone = forms.ModelChoiceField(queryset= Zone.objects.all())
    tags = forms.ModelChoiceField(queryset= Tag.objects.all(),required=False)
    add_a_location= forms.BooleanField(required=False)
    lng= forms.DecimalField(widget=forms.HiddenInput(),required=False)
    lat= forms.DecimalField(widget=forms.HiddenInput(),required=False)
    class Meta: 
        model = Post
        fields = ('title','author','sitspot','zone','image','tags','content', 'website',)

class CommentForm(forms.ModelForm):
    author = forms.CharField(max_length=255, required=True)
    # content = forms.CharField(min_length=1 ,widget=forms.Textarea, required=True)
    class Meta: 
        model = Comment
        fields = ('author','content')

class ReplyForm(forms.ModelForm):
    author = forms.CharField(max_length=255, required=True)
    content = forms.CharField(max_length=255, required=True)
    class Meta: 
        model = Reply
        fields = ('author','content')