from django.shortcuts import render
from homepage.forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.http import JsonResponse


#######################################
# Process Index request
#######################################
def index(request):
    return render(request, 'homepage/index.html')


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
            client_company = form.cleaned_data['contact_company']
            content = form.cleaned_data['content']
            content += '\nClient Name: ' + name
            content += '\nClient Company: ' + client_company
            content += '\nClient Email: ' + client_email
            content += '\nClient Contact Number: ' + client_number
            content += '\nPlease quick respond our clients (within 30 minutes) and collect the project requirements completely.\n'
            from_email = settings.EMAIL_HOST_USER
            to_email = ['steven.bb.0221@gmail.com']
            # attachment = request.FILES['attachment']
            attachment = form.cleaned_data['attachment']

            try:
                mail = EmailMessage(subject, content, from_email, to_email)
                if not attachment:
                    mail.send()
                else:
                    mail.attach(attachment.name, attachment.read(), attachment.content_type)
                    mail.send()
            except:
                return JsonResponse({'message': "Sorry, the executable file isn't allowed."})
            return JsonResponse({'message': "Thanks for your asking, we would get back to you as soon as possible."})
        else:
            explanation = form.errors['attachment']
            return JsonResponse({'message': explanation})
    else:
        form = ContactForm()

    return render(request, 'homepage/contact.html', {'form': form})



#######################################
# Process Case request
#######################################
def case(request):
    return render(request, 'homepage/case.html')


#######################################
# Process Case_show request
#######################################
def case_show(request):
    return render(request, 'homepage/case_show.html')


#######################################
# Process About request
#######################################
def about(request):
    return render(request, 'homepage/about.html')
