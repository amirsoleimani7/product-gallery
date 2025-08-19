from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 

def pagination(request):



    return render(request , 'index.html' , context={})

