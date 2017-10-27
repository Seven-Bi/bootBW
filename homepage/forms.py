from django import forms
from .attachment_check import verify_file


#################################
# Represent user contact form
#################################
class ContactForm(forms.Form):
    contact_name = forms.CharField(max_length=30, required=True)
    contact_email = forms.EmailField(required=True)
    contact_subject = forms.CharField(required=True)
    contact_number = forms.CharField(max_length=30, required=False)
    contact_company = forms.CharField(max_length=30, required=False)
    content = forms.CharField(widget=forms.Textarea, required=True)
    attachment = forms.FileField(required=False, validators=[verify_file])
