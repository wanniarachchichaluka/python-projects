#using while
i=0
while i<=2:
    print("meow")
    i+=1

#using for
for i in [0,1,2]:
    print("Meow")

#modifying for
for _ in range(9):
    print("Meow")

#another way
print(("meow\n") * 3,end="")

#getting a user input as a loop variable
while True:
    n=int(input("What's n? "))
    if n>0:
        break
for _ in range(n):
    print("meow")

######################################################
def main():
    num=get_num()
    meow(num)

def get_num():
    while True:
        n=int(input("What's n? "))
        if n>0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")
    

main()

#############################################


#Dictionary
students={
    "Herm":"Griff",
    "Harr":"Griff",
    "Ron":"Griff",
    "Drac":"Sly"
}

#print(students["Herm"])

for student in students:
    print(student,students[student],sep=" : ")
    
###################################################
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
