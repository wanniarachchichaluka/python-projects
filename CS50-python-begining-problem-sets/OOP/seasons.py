import sys
from datetime import date
import inflect
p=inflect.engine()

def main():
    try:
        mins=cal_mins(input("Date of Birth: "))
        print(p.number_to_words(mins,andword="").capitalize(),"minutes")
    except ValueError:
        sys.exit("Invalid input fotmat")

def cal_mins(d):
    y,m,d=d.split("-")
    y=int(y)
    m=int(m)
    d=int(d)
    
    bdayordinal=date.toordinal(date(y,m,d))
    tdordinal= date.today().toordinal()
    k=(tdordinal - bdayordinal)*24*60
    return k


if __name__ == "__main__":
    main()