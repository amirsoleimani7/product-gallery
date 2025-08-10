from django.shortcuts import render
from translate import Translator
import pyjokes


def traslate(request):

    text = ''
    to = ''
    if request.POST:
        print(f"text to translate is : {request.POST.get('text')}")
        print(f"to : {request.POST.get('lang')}")

        text = request.POST.get('text')
        to = request.POST.get('lang')


    translator = Translator(to_lang=to)
    translation = translator.translate(text)

    print(f"the translation is : {translation}")

    context= {
        'text' : text,
        'translation' :  translation ,
        'joke' : 
    }
    return render(request , 'translator/index.html' , context)

