from calendar_getter import *
from datetime import datetime, date, timedelta
from dateutil import tz

def date_to_datetime(dt, hour = 0, minute = 0, second = 0):
    timezone = tz.gettz('Europe/Paris')
    return datetime(
            dt.year, dt.month, dt.day, hour, minute, second, tzinfo =timezone
    )

def week_start():
    today = date.today()
    start = today - timedelta(days = today.weekday())
    return date_to_datetime(start)

def week_end():
    return week_start() + timedelta(days = 7)

def is_event_this_week(event):
    return week_start() <= event.begin <= week_end()

def week_events(contest):
    calendar = CALENDARS[contest]
    events = sorted(calendar.events)
    events = filter(is_event_this_week, events)
    return events
