import re

gd = """
    My name is Sanjeev kumar Rai.
    I belong to Bihar.I have completed B.Tech in 2018.
    My mobile number is 8578027159
    """
match_mob_no = re.findall(r'\d{10}', gd)
print(match_mob_no)