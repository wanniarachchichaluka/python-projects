class Student:
    def __init__(self,name,house=None):
        if not name:
            raise ValueError("Missing name")
        if house not in ["a","b","c","d"]:
            raise ValueError("Invalid house")
        self.name=name
        self.house=house
    def __str__(self):
        return f"{self.name} from {self.house}"

def main():
    student = get_student()
    print(f'{student.name} from {student.house}')
    print(student)

def get_student():
    name=input("Name: ")
    house = input("House: ")
    try:
        student = Student(name,house)
        return student
    except ValueError:
        ...
#or return Student(name,house )
        
if __name__=="__main__":
    main()
