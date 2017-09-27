from django import forms
from . import attachment_check


#################################
# Represent user contact form
#################################
class ContactForm(forms.Form):
    contact_subject = forms.CharField(max_length=100, required=True)
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Invalid contact number.")
    contact_number = forms.CharField(validators=[phone_regex], max_length=15, required=False)
    content = forms.TextField(required=False)
    # attachments check
    # <form enctype="multipart/form-data" method="post" action="/foo/"> integrate to html form element
    attachment = forms.FileField(validators=[attachment_check], required=False)
