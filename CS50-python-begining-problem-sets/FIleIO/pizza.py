import sys
from tabulate import tabulate
tabulate.PRESERVE_WHITESPACE = True
pizzas=[]
if len(sys.argv)<2:
    print("Too few args")
elif len(sys.argv)>2:
    print("Too many args")
else:
    try:
        if (sys.argv[1]).endswith('.csv'):
            with open(sys.argv[1],newline='') as file:
                for line in file:
                    sicilian_pizza, small, large = line.rstrip().split(",")
                    pizza = {"Sicilian Pizza":sicilian_pizza,"Small":small,"Large":large}
                    pizzas.append(pizza)
                print(tabulate(pizzas,headers="firstrow",tablefmt="grid"))    
        else:
            print("Wrong file type")
    except FileNotFoundError:
        sys.exit("File not found")
