import re

email = input("What's your email? ").strip()

#r means row string
#regex effecting from left
#if re.search(r".{1}.*@.*", email):
#if re.search(r"^[^@]+@[^@]+\.edu$", email):
#if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
#\w represents a word character [a-zA-Z0-9_]
#[a-zA-Z0-9_ ] or [\w|\s] for white space
#if re.search(r"^\w+@(\w+\.)?\w+\.edu$$", email, re.IGNORECASE):
if re.search(r"^\w+@(\w+\.)?\w+\.edu$$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")



