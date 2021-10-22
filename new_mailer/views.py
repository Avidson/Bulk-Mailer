from django.shortcuts import render
from .forms import EmailForm
from django.core.mail import EmailMessage, send_mail, send_mass_mail, BadHeaderError, EmailMessage
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
import ckeditor 
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.files import File 
from django.core import mail 

# Create your views here.


@login_required
def mail_sender(request):
    
    form = EmailForm(request.POST)
    sent = False
    connection.open()
    if request.method == 'POST':
        form = EmailForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            subject = request.POST.get(f"{cd['subject']}")
            message = request.POST.get(f"{cd['message']}")
            from_email = request.POST.get(f"{cd['from_email']}")
            bcc = request.POST.get(f"{cd['bcc']}")
            reply_to = request.POST.get(f"{cd['reply_to']}")
            fd = request.POST.get(f"{cd['attachment']}")
            with mail.get_connection() as connection:
                email = mail.EmailMessage(subject, message, from_email, [cd['to', 'to']],
                [cd['bcc']], reply_to=[cd['reply_to']], connection=connection).send()
                sent = True

            connection.send_messages(email)
            connection.close()
            res = email.send(fail_silently=False)
            res()
        
            
            
        else:
            form = EmailForm()

    context = {
        'form' : form,
        'sent' : sent

    }
    return render(request, 'new_mailer/send_mail.html', context)


def index_page(request, *args, **kwargs):

    return render(request, 'home.html', {})



