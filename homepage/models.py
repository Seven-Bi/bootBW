from django.db import models


class Client_Message():
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.TextField()
    email = models.EmailField()

    # any attachment user wants us to have a look.
    # need to specify the target location for storing the files.
    # (optional ?)
    attachment = models.FileField(upload_to='')
