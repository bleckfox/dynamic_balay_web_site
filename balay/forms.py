from django import forms

class Email(forms.Form):
    att = {'class': 'form-control'}
    name = forms.CharField(label='Name', min_length=2, max_length=100, widget=forms.TextInput(attrs = att))
    email = forms.EmailField(min_length=6, max_length=100, widget=forms.EmailInput(attrs=att))
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs = att))
    message = forms.CharField(widget=forms.Textarea(attrs = att))