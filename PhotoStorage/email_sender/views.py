from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    context = {}

    if request.POST:
        end_email = request.POST.get('address')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        print(f"end email is : {end_email}")
        print(f"subject is : {subject}")
        print(f"message is : {message}")


        
        if end_email and subject and message :
            try :
                send_mail(subject ,message , settings.EMAIL_HOST_USER ,[end_email]) 
                context['res'] = 'Email sent succesfully'
            except Exception as e:
                context['res'] = f'error sending email :{e}'
        else :  
            context['res'] = 'you should fill all the feilds'

    else :
        print(f'the request wast even post')


    return render(request ,'email_sender/index.html' , context)