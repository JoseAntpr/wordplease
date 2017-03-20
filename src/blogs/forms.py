from django import forms

from .models import Post, Blog


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "summary", "body", "media", "blog", "categories"]
    def __init__(self,user,*args,**kwargs):
        self.user = user
        super(PostForm, self).__init__(*args,**kwargs)
        self.fields['blog'].queryset = Blog.objects.filter(user=self.user)