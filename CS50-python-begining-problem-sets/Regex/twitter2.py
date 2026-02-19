import re

url = input("URL: ").strip()

uname= re.sub(r"^(https?://)?(www\.)?twitter\.com/","",url)
#but may fail with https://www.google.com/
print(f"Username: {uname}")