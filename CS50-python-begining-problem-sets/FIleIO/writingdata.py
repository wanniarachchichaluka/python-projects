import csv

name = input("What's the name: ")
home = input("WHere from? ")

with open("studentsWriting.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([name,home])

