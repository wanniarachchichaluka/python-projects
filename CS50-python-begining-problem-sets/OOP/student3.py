class Student:
    ...

def main():
    student = get_student()
    print(f'{student.name} from {student.house}')

def get_student():
    student = Student()#creating a new student object
    #adding parameters to the student object with user input.
    student.name = input("Name: ")
    student.house = input("House: ")
    return student
        
if __name__=="__main__":
    main()
