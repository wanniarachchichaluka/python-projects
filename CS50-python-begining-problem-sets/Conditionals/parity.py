

def main():
    x=int(input("What's x: "))
    if is_even(x):
        print("even x")
    else:
        print("odd x")

def is_even(n):
    return n%2==0
    
main()

#this one line also possible in python
#return True if n%2==0 else False