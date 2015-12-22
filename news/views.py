from django.shortcuts import render
from firebase.firebase import FirebaseApplication
from datetime import datetime
import time


# Create your views here
def home_firebase(request):
    title = "fess"
    # firebase = FirebaseApplication('https://your_storage.firebaseio.com', None)
    # firebase = firebase.FirebaseApplication('https://hacker-news.firebaseio.com', None)
    aFirebase = FirebaseApplication('https://hacker-news.firebaseio.com', None)
    print(aFirebase)
    result = aFirebase.get('/v0/item', "8952")
    itemTime = datetime.fromtimestamp(int(result['time']))
    present = datetime.now()

    newDate = datetime(2007,4,4)
    if present == newDate:
        print("OK")
    else:
        print("NotOK", present, newDate)

    if itemTime.date() == newDate.date():
        print('matching')


    context = {
        "title": title
    }


    return render(request, "news/home.html", context)