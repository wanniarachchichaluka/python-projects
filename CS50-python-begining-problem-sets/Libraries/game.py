import random
while 1:
    try:
        n=int(input("Level: "))
        if n>0:
            break
    except ValueError:
        continue


x=random.randint(1,n)
while 1:
    y=int(input("Guess: "))
    if y<x:
        print("Too small!")
    if y>x:
        print("Too large!")
    if x==y:
        print("Just right!")
        break