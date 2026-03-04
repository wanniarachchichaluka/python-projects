def main():
    student = get_student()
    if student["name"]=="Padma":
        student["house"]="Ravenclaw"
    print(f'{student["name"]} from {student["house"]}')

def get_student():
    student = {} #declaring the dictionary
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student
#or
#name = input("Name: ")
#house = input("House: ")
#return student["name":name,"house":house]
        
if __name__=="__main__":
    main()
