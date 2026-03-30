def convert(n):
    n = n.replace(':)','🙂') 
    n = n.replace(':(','🙁')
    return n
def main():
    n=input("")
    print(convert(n))

if __name__=="__main__":
    main()
