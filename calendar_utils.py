from datetime import datetime, date, timedelta
from dateutil import tz

def is_event_future(event):
    return event.begin >= datetime.now(event.begin.tzinfo)

def future_events(calendar):
    events = sorted(calendar.events)
    events = filter(is_event_future, events)
    return events

def timedelta_message(timedelta):
    seconds = timedelta.seconds
    minutes = seconds // 60
    hours = minutes // 60
    minutes %= 60
    days = timedelta.days
    result = ""
    if days == 1:
        result = "1 jour"
    if days > 1:
        result = f"{days} jours"
    if days > 0 and minutes + hours > 0:
        result += ", "
    if minutes + hours > 0:
        result += f"{hours}h{minutes:02d}"
    return result
