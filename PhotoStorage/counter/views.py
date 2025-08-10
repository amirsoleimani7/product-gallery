from django.shortcuts import render


def word_counter(request):
    
    text = ''

    if request.method == 'POST':
        print(f"the text is : {request.POST.get('mytest' , 'didnt get the thing')}")
        text = request.POST.get('mytest' , '')

    char_counter = 0

    if text:
        char_counter = text.count(" ") + 1
        print(f"there are {char_counter} in the text")
    else:
        print(f"there are non in the text")
    

    context = {
        'text' : text , 
        'char_counter' : char_counter , 
    }
    
    return render(request , 'counter/index.html' , context)

