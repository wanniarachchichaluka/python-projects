def main():
    yell("This","is","CS50")

def yell(*words):
    #functional programming where str.upper function is called on every one of 'words'
    uppercased = map(str.upper, words)
    print(*uppercased)

if __name__=="__main__":
    main() 