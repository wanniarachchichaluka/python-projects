#no need to instantiate an object from the class seperately if we define it as a class method
import random
class Hat:
    houses = ["a","b","c","d"]
    @classmethod
    def sort(cls, name):
        print(name, "is in",random.choice(cls.houses) )

#instantiating an object from a class
#hat = Hat() //no need of this 
Hat.sort("Harry")

#difference between instance method and class method?
#difference between class variables,methods and instance variables,methods?