def main():
    u_input=input("Input: ")
    f_output= shorten(u_input)
    print("Output: "+f_output)
def shorten(word):
    k=["a","e","i","o","u","A","E","I","O","U"]
    f_output=""
    for _ in range (len(word)):
        if word[_] not in k:
            f_output=f_output+word[_]
        else:
            continue
    return f_output
if __name__=="__main__":
    main()