import os
from django.core.exceptions import ValidationError


########################################
# checking attachment before upload
########################################
def verify_file(value):
    file_size = value.size
    # retrieve the extensions other than path+filename
    ext = os.path.splitext(value.name)[1]
    validate_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.bmp', '.png', '.pptx', 'xlsx', '.xls']
    if not ext.lower() in validate_extensions:
        raise ValidationError('Unsupported file type, please try .pdf, .doc, .docx, .xls, .xlsx, .jpg, etc.')
    if file_size > 10*1024*1024:
        raise ValidationError('Too large file > 10MB.')
