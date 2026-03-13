students = [
    {"name": "a", "house":"b",},
    {"name": "c", "house":"b",},
    {"name": "e", "house":"b",},
    {"name": "g", "house":"h",},
]

bs = filter(lambda s: s["house"] == "b", students)

for b in sorted(bs, key=lambda s: s["name"]):
    print(b["name"])

