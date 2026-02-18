x=input("Greeting: ")
y=str.lower(x)
if y.startswith('hello'):
    print("$0")
elif y[0]=='h' and y.startswith('hello')==False:
    print("$20")
else:
    print("$100")

