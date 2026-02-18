j=input("Expression: ")
x,y,z=j.split(" ")

match y:
    case "+":
        print(f"{(int(x)+int(z)):,.1f}")
    case "-":
        print(f"{(int(x)-int(z)):,.1f}")
    case "*":
        print(f"{(int(x)*int(z)):,.1f}")
    case "/":
        print(f"{(int(x)/int(z)):,.1f}")

    
    
