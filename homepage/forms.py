from django import forms
from .formfield_check import verify_file


#################################
# Represent user contact form
#################################
class ContactForm(forms.Form):
    contact_name = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class' : 'form_txt', 'placeholder' : 'Full name'}))
    contact_email = forms.EmailField(max_length=50, required=True, widget=forms.EmailInput(attrs={'class' : 'form_txt', 'placeholder' : 'Email address'}))
    contact_subject = forms.CharField(max_length=30, required=True, widget=forms.HiddenInput(attrs={'class' : 'inputselect', 'value' : "Website design"}))
    contact_number = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'class' : 'form_txt', 'placeholder' : 'Your contact number'}))
    contact_company = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'class' : 'form_txt', 'placeholder' : 'Company name'}))
    content = forms.CharField(min_length=15, widget=forms.Textarea(attrs={'class' : 'form_textarea', 'placeholder' : 'Descirbe your project details'}), required=True)
    attachment = forms.FileField(required=False, validators=[verify_file])
