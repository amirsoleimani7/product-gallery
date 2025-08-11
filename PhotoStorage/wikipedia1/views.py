from django.shortcuts import render
import wikipedia

def home(request):
    search_item = ''
    res = ''
    link = ''

    if request.method == "POST":
        search_item = request.POST.get('search')
        try:
            res = wikipedia.summary(search_item, sentences=1)
            link = wikipedia.page(search_item).url
            print(f"the result is: {res}")
            print(f"the link is: {link}")
        except wikipedia.exceptions.DisambiguationError as e:
            res = f"Your search term is ambiguous. Options: {e.options}"
        except wikipedia.exceptions.PageError:
            res = "No page found for your search."
        except Exception as e:
            res = f"An error occurred: {e}"

    context = {
        'res': res,
        'link': link,
    }

    return render(request, 'wikipedia/index.html', context)
