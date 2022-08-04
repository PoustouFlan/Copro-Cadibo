from secret import TOKEN
from calendar_utils import timedelta_message

ROLES = {
    "atcoder": 837746179138912307,
    "codechef": 835477747840974868,
    "codeforces": 835477747840974868,
    "codingame": 1004493089748033716,
    "google": 835480582384910366,
    "hackerrank": 1004493385396142110,
    "leetcode": 837745978378682448,
    "yukicoder": 837746728781611038,

    "botengineer": 1004491031628230756,
}

ADMIN = {
    427489795673948162,
}

CHANNELS = {
    "atcoder": 1001140362577985546,
    "codechef": 1004380321715847280,
    "codeforces": 1001140349776953464,
    "codingame": 1001140376901533796,
    "google": 1001140387580235877,
    "hackerrank": 1003419681450885312,
    "leetcode": 1003419750350717079,
    "topcoder": 1003419566917025814,
}

DISPLAY = {
    "atcoder": "[AtCoder]",
    "codechef": "[CodeChef]",
    "codeforces": "[Codeforces]",
    "codingame": "[CodinGame]",
    "google": "[Google]",
    "hackerrank": "[HackerRank]",
    "leetcode": "[LeetCode]",
    "topcoder": "[TopCoder]",
}

def admin_only(func):
    async def wrapper(ctx, *args, **kwargs):
        if ctx.author.id not in ADMIN:
            await ctx.send("403 forbidden")
            return False
        await func(ctx, *args, **kwargs)
    return wrapper

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
