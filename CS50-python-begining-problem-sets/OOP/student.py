def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house #or return (name,house)
#name, house is a one tuple, not seperate values. tuple is immutable
#or return [name,house] , list is muttable
        
if __name__=="__main__":
    main()
