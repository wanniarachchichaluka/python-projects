#alltogether 3 dictionaries
students = [
    #dic 1: a collection of key value pairs. 3 keys
    {"name":"Herm",
     "house":"Gryff",
     "patronus":"Otter"
    },
    #dic 2
    {"name":"Harry","house":"Gryff","patronus":"Stag"},
    #dic 3
    {"name":"Ron","house":"Gryff","patronus":"Jack Russel terrier"},
    #dic 4
    {"name":"Draco","house":"Slyth","patronus":None},
]

for student in students:
    print(student["name"],student["house"],student["patronus"],sep=":")