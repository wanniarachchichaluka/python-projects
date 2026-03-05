import random
class Hat:
    def __init__(self):
        self.houses = ["a","b","c","d"]
    def sort(self, name):
        print(name, "is in",random.choice(self.houses) )

#instantiating an object from a class
hat = Hat() 
hat.sort("Harry")