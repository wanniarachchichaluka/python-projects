def main():
    u = input("What time is it? ")
    n=float(convert(u))
    if n>= 7.00 and n<=8.00:
        print("breakfast time")
    if n>=12.00 and n<=13.00:
        print("lunch time")
    if n>=18.00 and n<=19.00:
        print("dinner time")
def convert(time):
    x,y = time.split(":")
    v=float(y)/60
    b=float(x)+v
    return f"{b:,.2f}"
if __name__== "__main__":
    main()