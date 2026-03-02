import re
import sys


def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        sys.exit("invalid")

def convert(s):
  
        matches6 = re.search(r'(^[1-9]{1,2}):*([0-9]{2})* AM.[^0-9]+([1-9]{1,2}):*([0-9]{2})*',s)
        a=int(matches6.group(1))
        c=int(matches6.group(3))

        if matches6.group(2)==None:
            b=0
        else:
            b=int(matches6.group(2))
        
        if matches6.group(4)==None:
            d=0
        else:
            d=int(matches6.group(4))

        if a>=13 or c>=13:
            raise ValueError
        if b>59 or d>59:
            raise ValueError
        j=12+c
        return f"{a:02d}:{b:02d} to {j}:{d:02}"
    

if __name__ == "__main__":
    main()