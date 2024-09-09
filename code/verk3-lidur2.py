import re


# Regluleg segð fyrir almenn netföng
pattern = r'[a-zA-Z0-9þæð_.+-]+@[a-zA-Zþæð0-9-]+\.[a-zA-Zþæð0-9-.]+'

with open('code\skra.txt', 'r', encoding='utf-8') as file:
    texti = file.read()


# Nota findall til að finna öll netföng í textanum
netfong = re.findall(pattern, texti)

print(netfong)
