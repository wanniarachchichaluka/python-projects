def main():
    yell(["This","is","CS50"])#list of words

def yell(words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(uppercased)
    print(*uppercased)

if __name__=="__main__":
    main() 