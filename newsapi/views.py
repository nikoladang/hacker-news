from django.shortcuts import render
from django.conf import settings
import requests
from datetime import datetime
from operator import itemgetter
import json

# Create your views here.
from .forms import SubmitEmbed
from .serializer import EmbedSerializer

def get_story(timestamp1, timestamp2):
    # url = 'http://hn.algolia.com/api/v1/search_by_date?tags=story&numericFilters=created_at_i>'+str(timestamp1)+',created_at_i<'+str(timestamp2)
    url = 'http://hn.algolia.com/api/v1/search_by_date?tags=story&hitsPerPage=2000&numericFilters=created_at_i>{0},created_at_i<{1}'.format(str(timestamp1), str(timestamp2))
    r = requests.get(url)
    jsonResult1 = r.json()
    # print(jsonResult1)
    print(jsonResult1['nbHits'])
    # print(jsonResult1['hitsPerPage'])
    # print(json.__len__())
    result = jsonResult1['hits']
    return result

def newsapi_home(request):

    # r = requests.get('http://hn.algolia.com/api/v1/search?query=foo&tags=story')
    # print(r.status_code)
    date1 = datetime(2015,12,19).timestamp()
    date2 = datetime(2015,12,19,23,59,59).timestamp()
    # print(date2-date1)
    result = get_story(date1,date2)
    newlist = sorted(result, key=itemgetter('points'), reverse=True)
    print(json.dumps(newlist, indent=2))

    return render(request, "news/home.html", {})
