class Student:
    def __init__(self,name,house,patronus=None):
        if not name:
            raise ValueError("Missing name")
        if house not in ["a","b","c","d"]:
            raise ValueError("Invalid house")
        self.name=name
        self.house=house
        self.patronus=patronus
    def __str__(self):
        return f"{self.name} from {self.house}"
    def charm(self):
        match self.patronus:
            case "Stag":
                return "🤣"
            case "Otter":
                return "😒"
            case _:
                return "🤩"
def main():
    student = get_student()
    print("Expectro Patronum!")
    print(student.charm())

def get_student():
    name=input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    try:
        student = Student(name,house,patronus)
        return student
    except ValueError:
        ...
#or return Student(name,house )
        
if __name__=="__main__":
    main()
