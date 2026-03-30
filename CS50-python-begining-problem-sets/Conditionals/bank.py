def main():
    x=input("Greeting: ")
    print(f"${value(x)}")

def value(greeting):
    y=greeting.strip().lower()
    if y.startswith('hello'):
        return 0
    elif y[0]=='h' and y.startswith('hello')==False:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()