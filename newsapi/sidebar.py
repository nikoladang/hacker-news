from datetime import datetime, timedelta

"""
Return a list of dictionaries of 3 dates before, 3 dates after current date
"""
def date_to_dict(adate):
    dict = {}
    dict["year"] = adate.strftime("%Y")
    dict["month"] = adate.strftime("%m")
    dict["day"] = adate.strftime("%d")

    return dict

def get_sidebarDates(year, month, day):
    inputDate = datetime(int(year),int(month),int(day))
    curDate = datetime.now().date()
    sidebarDates = []

    for i in reversed(range(1,4)):
        newDate = inputDate+timedelta(days=i)
        if newDate.date() <= curDate-timedelta(days=1):
            sidebarDates.append(date_to_dict(newDate))

    sidebarDates.append(date_to_dict(inputDate))

    for i in range(1,4):
        newDate = inputDate-timedelta(days=i)
        sidebarDates.append(date_to_dict(newDate))

    return sidebarDates
