from django.shortcuts import render
from homepage.forms import ContactForm
from django.core.mail import send_mail, EmailMessage
from django.http import JsonResponse


#######################################
# Process user contact form request
#######################################
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            subject = form['contact_subject']
            name = form['contact_name']
            email = form['contact_email']
            phone_number = form['contact_number']
            content = form['content']
            attachment = request.FILES['attachment']
            try:
                mail = EmailMessage(subject, content, ['bootBW2017@gmail.com'], email)
                mail.attach(attachment.name, attachment.read(), attachment.content_type)
                mail.send()
            except:
                return JsonResponse({'message': "Failed to send email, please check with your email."})
            return JsonResponse({'message': "Thanks for your asking, we would get back to you as soon as possible."})
        else:
            return return JsonResponse({'message': "Some errors happened, please call +610450980608."})
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
