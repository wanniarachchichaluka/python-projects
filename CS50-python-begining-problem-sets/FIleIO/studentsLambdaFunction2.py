import csv

students = []

with open("students2.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name":name, "home":home})

print(students)

#each of student is a dictionary
for student in sorted(students,key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")