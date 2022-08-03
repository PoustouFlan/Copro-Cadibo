from secret import TOKEN
from calendar_utils import timedelta_message

ROLES = {
    "codeforces": 835477747840974868,
    "yukicoder": 837746728781611038,
    "codejam": 835480582384910366,
    "atcoder": 837746179138912307,
    "leetcode": 837745978378682448,
}

ADMIN = {
    427489795673948162,
}

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

def event_message(event, contest):
    name = event.name
    begin = event.begin
    duration = event.duration
    description = event.description
    duration_message = timedelta_message(duration)
    if description != '':
        description = ">>> " + description
    
    return (
        f"───────────────────────────\n"
        f"{mention_role(contest)}\n"
        f"**{name}**\n\n"
        f"{arrow_to_timestamp(begin)} ({arrow_to_countdown(begin)})\n"
        f"{duration_message}\n"
        f"{description}\n"
    )


