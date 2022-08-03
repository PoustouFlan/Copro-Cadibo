
ROLES = {
    "codeforces": 835477747840974868,
    "yukicoder": 837746728781611038,
    "codejam": 835480582384910366,
    "atcoder": 837746179138912307,
    "leetcode": 837745978378682448,
}

def mention_role(name):
    if name is None:
        return ''
    identifier = name.lower().replace(' ', '')
    if identifier not in ROLES:
        return "@" + name
    return f"<@&{ROLES[identifier]}>"
