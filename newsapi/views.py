from django.shortcuts import render
from django.conf import settings
import requests
from datetime import datetime, date, timedelta
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
    # print(jsonResult1['nbHits'])
    # print(jsonResult1['hitsPerPage'])
    # print(json.__len__())
    result = jsonResult1['hits']
    return result


def newsapi_home(request):

    today = datetime.now()
    curYear = today.year
    curMonth = today.month
    curDay = today.day
    date1 = datetime(curYear,curMonth,curDay-1).timestamp()
    print(type(date1))
    date2 = datetime(curYear,curMonth,curDay-1,23,59,59).timestamp()
    print(date2)

    # # currentDate = date.today()
    # currentDate = datetime.now()
    # print(currentDate.date().ctime())
    # print(currentDate)
    # print(date1)
    # print(date2)
    # date3 = (currentDate - timedelta(days=1)).timetuple()
    # print(date3)
    # # print(date2-date1)
    # # for item in newlist:
    # #     print(item['title'])
    # #     print(item['url'])
    # #     print(item['objectID'])

    result = get_story(date1,date2)
    newlist = sorted(result, key=itemgetter('points'), reverse=True)[:10]
    # print(json.dumps(newlist, indent=2))

    newdict = {}
    newdict['hnDate'] = datetime.fromtimestamp(date1).strftime('%Y-%d-%m')
    print(newdict['hnDate'])
    newdict['hnValue'] = newlist
    print(type(newlist))
    resultList = []
    resultList.append(newdict)
    print(newdict)


    return render(request, "news/home2.html", {"result": resultList})
