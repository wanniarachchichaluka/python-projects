students = [
    {"name": "a", "house":"b",},
    {"name": "c", "house":"b",},
    {"name": "e", "house":"b",},
    {"name": "g", "house":"h",},
]

bs = [
    student["name"] for student in students if student["house"]=="b"
]

for b in sorted(bs):
    print(b)