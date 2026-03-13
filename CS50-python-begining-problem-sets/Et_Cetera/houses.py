#list of dictionaries
students = [
    {"name": "Chaluka", "house": "Kurunegala"},
    {"name": "Pamintha", "house": "Colombo"},
    {"name": "Wanniarachchi", "house": "America"},
    {"name": "Kelum", "house": "Switzerland"},
]

#empty list
houses = []

for student in students:
    if student["house"] not in houses:
        houses.append(student["house"])

for house in sorted(houses):
    print(house)