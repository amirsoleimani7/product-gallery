from django.shortcuts import render

def home(request):

    email = ''
    sub = ''
    unsub = '' 

    if request.POST:

        email = request.POST.get('email')
        sub = request.POST.get('subscribe')
        unsub = request.POST.get('unsubscribe')

        print(f"the user's email is : {email}")
        print(f"the sub button is : {sub}")
        print(f"the unsub button is : {unsub}")

    print(f"type of sub is : {type(sub)} , {type(unsub)}")


    if sub:
        print("person subed")
    if unsub:
        print("person unsubed")



    return render(request , 'multi_input/index.html' , context= {})
