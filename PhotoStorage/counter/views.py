from django.shortcuts import render , HttpResponse
from .forms import ContactForm

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
        'form' : ContactForm() , 
    }
    return render(request , 'counter/index.html' , context)

# adding google recapcha ... 
# def contact(request):
#     if request.method == 'POST':
#         form  = ContactForm(request.POST)
#         if form.is_valid():
#             return HttpResponse("u r a human")
#         else :
#             return HttpResponse('u are a bot ma dude')
#     else:
#         form = ContactForm()

#     return render(request , 'counter/index.html' , {'form' : form})