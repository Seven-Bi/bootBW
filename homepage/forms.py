from django import forms
from .attachment_check import verify_file


#################################
# Represent user contact form
#################################
class ContactForm(forms.Form):
    contact_subject = forms.CharField(max_length=100, required=True)
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    contact_number = forms.CharField(widget=forms.Textarea, required=False)
    content = forms.CharField(widget=forms.Textarea, required=True)
    attachment = forms.FileField(required=False, validators=[verify_file])
