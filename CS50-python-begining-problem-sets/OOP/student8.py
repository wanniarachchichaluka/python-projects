class Student:
    def __init__(self,name,house):
        self.name=name
        self.house=house 

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    #if its a class method use cls
    #class methods operate on all objects on that class while instance objects operate only on particular objects
    @classmethod #able to call this method without instantiating a student object
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)
    
def main():
    student = Student.get()
    print(student)
            
if __name__=="__main__":
    main()


##@staticmethod? **learn 
#@staticmethod
#    def is_legal_name(name):
#        # I don't need 'self' or 'cls' to check if a string is valid
#        return len(name) > 1

