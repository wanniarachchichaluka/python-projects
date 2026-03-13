#dynamically generate some brand new list for me
def main():
    yell("This","is","CS50")

def yell(*words):
    #storing in this list the uppercase version of every word in that word list
    uppercased = [word.upper() for word in words]
    print(*uppercased)

if __name__=="__main__":
    main() 