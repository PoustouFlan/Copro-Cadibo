from requests import get
from ics import Calendar
from sys import stderr

def debug(*args, **kwargs):
    print(*args, **kwargs, file = stderr)


ICS_URLS = {
    "codeforces": "https://calendar.google.com/calendar/ical/br1o1n70iqgrrbc875vcehacjg%40group.calendar.google.com/public/basic.ics",
    #"codechef": "https://calendar.google.com/calendar/ical/ogc7qt4hlg454ggkj9o6ttqnq8%40group.calendar.google.com/public/basic.ics",
}

CALENDARS = {}

for contest, url in ICS_URLS.items():
    debug(f"Requesting {contest} ics...")
    ics = get(url).text
    debug(f"Parsing {contest} ics...")
    calendar = Calendar(ics)
    CALENDARS[contest] = calendar
