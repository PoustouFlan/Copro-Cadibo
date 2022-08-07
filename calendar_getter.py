from requests import get
from ics import Calendar
from yaml import safe_load

import logging
log = logging.getLogger("zn30.utils")

configuration_file = open("calendars.yaml", "r")
configuration = safe_load(configuration_file.read())

CONTESTS = configuration['contests']
ICS_URLS = configuration['ics_urls']

def get_calendars(contests = CONTESTS):
    calendars = {}
    for contest in contests:
        url = ICS_URLS[contest]
        log.info(f"Requesting {contest} ics...")
        ics = get(url).text
        log.info(f"Parsing {contest} ics...")
        calendar = Calendar(ics)
        calendars[contest] = calendar
    return calendars
