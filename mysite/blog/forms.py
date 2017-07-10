from django import forms
from blog.models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('author', 'title', 'text')

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),  #给form添加class属性textinputclass是自定义的class
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}) #postcontent也是自定义的属性
        }



class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }
