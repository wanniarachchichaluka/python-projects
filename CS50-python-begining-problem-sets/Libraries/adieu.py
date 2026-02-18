list1=[]
import inflect
p=inflect.engine()
try:
    while 1:
        x=input("Name: ")
        if len(x)!=0:
            list1.append(x)
except EOFError:

    print("Adieu, adieu, to "+p.join(list1))