from django.shortcuts import render
from homepage.forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.http import JsonResponse


#######################################
# Process user contact form request
#######################################
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            subject = form.cleaned_data['contact_subject']
            name = form.cleaned_data['contact_name']
            client_email = form.cleaned_data['contact_email']
            client_number = form.cleaned_data['contact_number']
            content = form.cleaned_data['content']
            content += '\nClient Name: ' + name
            content += '\nClient Email: ' + client_email
            content += '\nClient Contact Number: ' + client_number
            content += '\nPlease quick respond our clients (within 1 hour) and collect rough project requirements\nAt the end, schedule the next contact time and let our clients know.'
            from_email = settings.EMAIL_HOST_USER
            to_email = ['steven.bb.0221@gmail.com']
            attachment = request.FILES['attachment']

            try:
                mail = EmailMessage(subject, content, from_email, to_email)
                if attachment:
                    mail.attach(attachment.name, attachment.read(), attachment.content_type)
                mail.send()
            except:
                return JsonResponse({'message': "Some errors happened, please call +610450980608."})
            return JsonResponse({'message': "Thanks for your asking, we would get back to you as soon as possible."})
        else:
            explanation = form.errors['attachment']
            return JsonResponse({'message': explanation})
    else:
        form = ContactForm()

    return render(request, 'contact/gettouch.html', {'form': form})
