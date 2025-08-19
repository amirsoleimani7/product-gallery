from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
from .models import Post


def pagination(request):
    posts = Post.objects.all()
    p = Paginator(posts , 5)

    page_number  = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    
    context = {
        'page_obj' : page_obj
    }

    return render(request , 'index.html' , context)
