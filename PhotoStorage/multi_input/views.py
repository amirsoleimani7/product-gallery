from django.shortcuts import render
from .models import NewsEmail


def home(request):

    email = ''
    sub = ''
    unsub = '' 

    if request.POST:

        email = request.POST.get('email')
        sub = request.POST.get('subscribe')
        unsub = request.POST.get('unsubscribe')

        if sub:
            print(f"person subed to :  {email}")
            new_emial = NewsEmail()
            new_emial.user_email = email
            new_emial.save()


        elif unsub:

            print(f"person unsubed from :  {email}")
            try :
                wanted_email = NewsEmail.objects.filter(user_email=email)
                print(f"the email is : {wanted_email}")
                wanted_email.delete()
                
           
            except:
                print(f"there was som erroes")


           


    return render(request , 'multi_input/index.html' , context= {})
