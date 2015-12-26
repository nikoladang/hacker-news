from django.shortcuts import render
from django.conf import settings
import requests
from datetime import datetime, date, timedelta
from operator import itemgetter
# import json
from .sidebar import get_sidebarDates

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

'''
Get top stories from HN with highests points in a specific day
Return: dict
'''
def get_top_stories_single_day(year, month, day, story_count=10):
    begintime = datetime(year,month,day-1).timestamp()
    endtime = datetime(year,month,day-1,23,59,59).timestamp()
    aList = get_story(begintime,endtime)
    sortedHnValueList = sorted(aList, key=itemgetter('points'), reverse=True)[:story_count]
    dictResult = {}
    # newdict['hnDate'] = datetime.fromtimestamp(date1).strftime('%Y-%d-%m')
    dictResult['hnDate'] = datetime(year,month,day).strftime('%Y-%m-%d')
    dictResult['hnValue'] = sortedHnValueList
    return dictResult


'''
Get top stories from HN with highests points in a specific day
Return: a list of dicts
'''
def get_top_stories_multi_days(year, month, day, day_count=3, story_count=10):
    resultList = []
    for i in range(day_count):
        resultList.append(get_top_stories_single_day(year,month,day-i, story_count))
    return resultList


def newsapi_home(request):
    today = datetime.now()
    curYear = today.year
    curMonth = today.month
    curDay = today.day

    # print(json.dumps(newlist, indent=2))


    chosenDate = (today-timedelta(days=1)).strftime("%Y-%m-%d")
    sidebarDates = get_sidebarDates(curYear,curMonth,curDay-1)
    resultList2 = get_top_stories_multi_days(curYear, curMonth, curDay-1, day_count=0)

    context = {
        "chosenDate": chosenDate,
        "sidebarDates": sidebarDates,
        "result": resultList2
    }
    return render(request, "news/home2.html", context)


def newsapi_home_adate(request, year, month, day):

    chosenDate = datetime(int(year),int(month),int(day)).strftime("%Y-%m-%d")
    sidebarDates = get_sidebarDates(year,month,day)
    resultList = get_top_stories_multi_days(int(year), int(month), int(day), day_count=1)

    print(sidebarDates)

    # print(sidebarDates)
    context = {
        "chosenDate": chosenDate,
        "sidebarDates": sidebarDates,
        "result": resultList
    }
    return render(request, "news/home2.html", context)