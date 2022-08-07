from calendar_utils import timedelta_message
from yaml import load

configuration_file = open("configuration.yaml", "r")
configuration = load(configuration_file.read())

TOKEN = configuration['token']
ROLES = configuration['roles']
CHANNELS = configuration['channels']
DISPLAY = configuration['display']

def contest_icon(contest):
    try:
        file = open(f"icons/{contest}.png", 'rb')
    except FileNotFoundError:
        return None
    return file.read()
        
def mention_role(name):
    if name is None:
        return ''
    identifier = name.lower().replace(' ', '')
    if identifier not in ROLES:
        return "@" + name
    return f"<@&{ROLES[identifier]}>"

def arrow_to_timestamp(arrow):
    unix = int(arrow.timestamp())
    return f"<t:{unix}>"

def arrow_to_countdown(arrow):
    unix = int(arrow.timestamp())
    return f"<t:{unix}:R>"
