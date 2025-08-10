from django.shortcuts import render


def traslate(request):


    context= {}
    return render(request , 'translator/index.html' , context)

