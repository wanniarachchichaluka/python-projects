#list of dictionaries
students = [
    {"name": "Chaluka", "house": "Kurunegala"},
    {"name": "Pamintha", "house": "Colombo"},
    {"name": "Wanniarachchi", "house": "America"},
    {"name": "Kelum", "house": "Switzerland"},
]

#set automatically eleminate duplicates
houses = set()

for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)