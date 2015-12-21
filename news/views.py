from django.shortcuts import render
from firebase.firebase import FirebaseApplication


# Create your views here
def home(request):
    title = "fess"
    # firebase = FirebaseApplication('https://your_storage.firebaseio.com', None)
    # firebase = firebase.FirebaseApplication('https://hacker-news.firebaseio.com', None)
    aFirebase = FirebaseApplication('https://hacker-news.firebaseio.com', None)
    print(aFirebase)
    # result = aFirebase.get('/v0/user', "jl", {'print': 'pretty'})
    # result = aFirebase.get('/v0/user', "jl", {'print': 'pretty'}, {'X_FANCY_HEADER': 'VERY FANCY'})
    result = aFirebase.get('/v0/user/jl', None)
    print(result)

    context = {
        "title": title
    }


    return render(request, "news/home.html", context)