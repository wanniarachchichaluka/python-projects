import random

def main():
    list1=[]
    list2=[]
    list3=[]
    level=get_level()
    num=generate_integer(level)
    for i in range(0,10):
        list1.append(generate_integer(level))
        list2.append(generate_integer(level))
        print(list1)
        print(list2)
    i=0
    count=0
    while i<10:
        try:
            print(f"{list1[i]} + {list2[i]} = ",end="")
            answer=int(input())
            while answer !=(list1[i]+list2[i]):
                print("EEE")
                print(f"{list1[i]} + {list2[i]} = ",end="")
                answer=int(input())
                if i not in list3:
                    list3.append(i)
            i=i+1
        except ValueError:
            if i not in list3:
                list3.append(i)
            print("EEE")
            continue
    print("Score: ",10-len(list3))
def get_level():
    while 1:
        level=int(input("enter level: "))
        if level in range(1,3):
            break
    return level

def generate_integer(level):
    rangeStart=10**(level-1)
    rangeEnd=(10**(level))-1
    return random.randint(rangeStart,rangeEnd)
if __name__ == "__main__":
    main()

