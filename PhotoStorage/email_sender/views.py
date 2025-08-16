from django.shortcuts import render



def home(request):

    return render(request ,'email_sender/index.html' , context = {})