def convert(fraction):
    x,y=fraction.split("/")
    try:
        a=int(x)
        b=int(y)

        if a < 0 or b < 0 :
            raise ValueError
        if b == 0:
            raise ZeroDivisionError
        if a > b:
            raise ValueError
        return int(round(100*(a/b)))
    except ValueError:
        return -1
    except ZeroDivisionError:
        return -1
    except TypeError:
        return -1

def gauge(percentage):
    if int(percentage)<=1:
        return "E"
    elif int(percentage)>=99:
        return "F"
    else:
        return f"{percentage}%"
def main():
    while True:
        fraction=input("Fraction: ")
        if convert(fraction)==-1:
            continue
        else:
            print(gauge(convert(fraction)))
            break

if __name__=="__main__":
    main()
