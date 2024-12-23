from django import forms


class PostForm(forms.Form):
    image = forms.FileField()
    text = forms.CharField(label='Description')
    # add class to form fields
    image.widget.attrs.update({'class': 'form-control'})
    text.widget.attrs.update({'class': 'form-control'})