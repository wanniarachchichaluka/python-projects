#yield "return one value at a time instead of returning all at once"
#advantage: program is not hanging
#yield -> iterators (one element at a time)
def main():
    n = int(input("Whats n? "))
    for s in sheep(n):
        print(s)
#🐏
def sheep(n):
    for i in range(n):
        yield "🐏" * i

if __name__=="__main__":
    main()