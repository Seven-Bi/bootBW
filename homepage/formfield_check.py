import os
from django import forms


########################################
# checking attachment before upload
########################################
def verify_file(value):
    file_size = value.size
    ext = os.path.splitext(value.name)[1]
    validate_extensions = ['.txt', '.pdf', '.doc', '.docx', '.jpg', '.bmp', '.png', '.pptx', '.xlsx', '.xls', '.zip', '.rar']
    if not ext.lower() in validate_extensions:
        raise forms.ValidationError('Unsupported file type, please try .pdf, .doc, .docx, .xls, .xlsx, .jpg, etc.')
    if file_size > 20*1024*1024:
        raise forms.ValidationError('Too large file > 20MB.')
