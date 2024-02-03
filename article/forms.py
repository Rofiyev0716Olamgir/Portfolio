from django import forms

from .models import Comments


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['massage', 'image', 'email', 'name']
        exclude = ['article']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['massage'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Write Comment',
            'rows': 9,
            'cols': 30,
            'name': 'massage',
            'id': 'massage'
            })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'name': 'email',
            'id': 'email',
            'placeholder': 'Enter email address',
            })
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your name',
            'name': 'name',
            'id': 'name',

        })
        self.fields['image'].widget.attrs.update({
            'class': 'form-image',
            'placeholder': 'Enter your image',
        })



