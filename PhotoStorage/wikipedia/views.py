from django.shortcuts import render
import wikipedia

def home(request):



    context = {}


    return render(request , 'wikipedia/index.html' , context)