students = [
    {"name": "a", "house":"b",},
    {"name": "c", "house":"b",},
    {"name": "e", "house":"b",},
    {"name": "g", "house":"h",},
]

def is_b(s):
    return s["house"]=="b"

bs = filter(is_b, students)

for b in sorted(bs, key=lambda s: s["name"]):
    print(b["name"])

