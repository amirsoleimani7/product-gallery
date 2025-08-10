from django.shortcuts import render


def word_counter(request):
    
    if request.method == 'POST':
        print(f"the text is : {request.POST.get('mytest' , 'didnt get the thing')}")
    context = {}

    return render(request , 'counter/index.html' , context)

