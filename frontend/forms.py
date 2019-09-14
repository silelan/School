from django import forms

'''class ContactForm(forms.Form):
    name = forms.CharField(required = False, max_length = 100, help_text = '100 character maximum')
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    comment = forms.CharField(widget=forms.Textarea, required=True)
'''


class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)