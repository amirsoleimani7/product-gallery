from django.shortcuts import render


def word_counter(request):
    
    print('we are in the coutner section for shue')
    context = {}

    return render(request , 'counter/index.html' , context)

