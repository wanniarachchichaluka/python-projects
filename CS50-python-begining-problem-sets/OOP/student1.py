import sys
class Student:
    def __init__(self,name,house):
        self.name=name
        self.house=house 

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("no name")
        self._name=name

    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self,house):
        if house not in ["a","b","c","d"]:
            raise ValueError("Invalid house")
        self._house=house

def main():
    student = get_student()
    student._house = "Number four" #little manipulation to run the code without error
    print(student)

def get_student():
    name=input("Name: ")
    house = input("House: ")

    student = Student(name,house)
    return student
            
if __name__=="__main__":
    main()

################# 1.39.00