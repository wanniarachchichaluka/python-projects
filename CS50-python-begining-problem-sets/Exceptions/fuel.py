def get_input():
    fraction=input("Fraction: ")
    numirator=""
    denominator=""
    l=0

    for f in range(len(fraction)):
        if fraction[f]=="/":
            l=1
            continue
        if l==0:
            numirator=numirator+fraction[f]
        if l==1:
            denominator=denominator+fraction[f] 

    try:
        a=int(numirator)
        b=int(denominator)

        if a < 0 or b < 0 :
            raise ValueError
        if b == 0:
            raise ZeroDivisionError
        if a > b:
            raise ValueError
        return a,b
    except ValueError:
        pass
    except ZeroDivisionError:
        pass

def get_fuel_pcntg():
    while True:
        try:
            a,b = get_input()
            return int(round(100*(a/b)))
        except TypeError:
            pass

def main():
    y = get_fuel_pcntg()
    if y<=1:
        print("E")
    elif y>=99:
        print("F")
    else:
        print(f"{y}%")

main()
