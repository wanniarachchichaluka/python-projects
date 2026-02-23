import re

url = input("URL: ").strip()



if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)",url,re.IGNORECASE):
    print(f"Username:",matches.group(1))


########################
if matches := re.search(r"^[0-255$","255"):
    print(matches)
