import sys
class Student:
    def __init__(self,name,house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["a","b","c","d"]:
            raise ValueError("Invalid house")
        self.name=name
        self.house=house #self.house also call particular setter

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

    #Getter is function in a calss that get a value
    ##You need a place to actually store the data that is 
    # different from the property name. If the property is house, 
    # the storage is _house.
    @property
    def house(self):
        return self._house
    
    #Setter
    @house.setter
    def house(self,house):
        if house not in ["a","b","c","d"]:
            raise ValueError("Invalid house")
        self._house=house

def main():
    student = get_student()
    student.house = "c" #student.house automatically call the setter
    print(student)

def get_student():
    name=input("Name: ")
    house = input("House: ")

    student = Student(name,house)
    student.house="b"
    return student
    
#or return Student(name,house )
        
if __name__=="__main__":
    main()
