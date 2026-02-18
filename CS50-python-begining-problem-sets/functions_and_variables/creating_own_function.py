name=input("What's your name: ")
def hello(to="world"):
    print("hello, "+to)
hello()
hello(name)


#######################################################################

def main():
    name=input("What's your name: ")
    hello()
    hello(name)
    num1=int(input("Enter a number: "))
    num2=int(input("Enter a number: "))
    added=calculator(num1,num2)
    print("addition of those two numbers = ",added)


def hello(to="world"):
    print("hello, "+to)

def calculator(num1=0,num2=0):
    return num1+num2
main()
