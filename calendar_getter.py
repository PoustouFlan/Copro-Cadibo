from requests import get
from ics import Calendar
from sys import stderr

def debug(*args, **kwargs):
    print(*args, **kwargs, file = stderr)


ICS_URLS = {
    "atcoder": "https://calendar.google.com/calendar/ical/vdobhfoodrv59522b684lhfs7c%40group.calendar.google.com/public/basic.ics",
    "codechef": "https://calendar.google.com/calendar/ical/ogc7qt4hlg454ggkj9o6ttqnq8%40group.calendar.google.com/public/basic.ics",
    "codeforces": "https://calendar.google.com/calendar/ical/br1o1n70iqgrrbc875vcehacjg%40group.calendar.google.com/public/basic.ics",
    "leetcode": "https://calendar.google.com/calendar/ical/tlvovsip3t3045rnkq0rt7d77c%40group.calendar.google.com/public/basic.ics",
    "topcoder": "https://calendar.google.com/calendar/ical/qshn4jb7pq3f8l46nvvilj5c6o%40group.calendar.google.com/public/basic.ics",
    "google": "https://calendar.google.com/calendar/ical/7qk9j0n6sa9hkc6hfgiho0m6og%40group.calendar.google.com/public/basic.ics",
}

CALENDARS = {}

for contest, url in ICS_URLS.items():
    debug(f"Requesting {contest} ics...")
    ics = get(url).text
    debug(f"Parsing {contest} ics...")
    calendar = Calendar(ics)
    CALENDARS[contest] = calendar
