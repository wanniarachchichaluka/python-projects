import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
list1=figlet.getFonts()

if len(sys.argv)==1:
    j=random.choice(list1)
    f=Figlet(font=j)
    n=input("Enter a str of text: ")
    print(f.renderText(n))
elif len(sys.argv)==3:
    if sys.argv[1]=='-f' or sys.argv[1]=='--font':
        if sys.argv[2] in list1:
            f=Figlet(font=sys.argv[2])
            n=input("Enter a str of text: ")
            print(f.renderText(n))
        else:
            sys.exit("invalid usage")
    else:
        sys.exit("invalid usage")    
else:
    sys.exit("Invalid usage")      
 

    