url = input("URL: ").strip()

#uname = url.replace("https://twitter.com/","")
uname = url.removeprefix("https://twitter.com/")
print(f"Username: {uname}")