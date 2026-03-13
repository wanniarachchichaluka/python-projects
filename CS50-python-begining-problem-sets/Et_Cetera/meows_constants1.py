#Python is a dynamically typed language.
#it automatically finds if a variable is int or float or etc.
class Cat:
    MEOWS=3 #a class variable

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")

cat = Cat()
cat.meow()

