from django.shortcuts import render
from homepage.forms import ContactForm
from django.core.mail import send_mail
from django.http import JsonResponse


#######################################
# Process user contact form request
#######################################
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form['contact_subject']
            name = form['contact_name']
            email = form['contact_email']
            phone_number = form['contact_number']
            content = form['content']
            attachment = form['attachment']
            send_mail()
            return JsonResponse({'message': "Thanks for your asking, we would get back to you as soon as possible."})
        else:
            return return JsonResponse({'message': "Some errors happened, please call +610450980608."})
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
