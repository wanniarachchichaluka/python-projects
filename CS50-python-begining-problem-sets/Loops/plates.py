
def chk_start(s):
    for _ in range(1):
        if 65<=ord(s[_])<=90:
            return True
    return False

def chk_len(s):
    if 2<=len(s)<=6:
        return True
    else:
        return False
    
def chk_zero(s):
    j=len(s)
    for i in range(len(s)):
        if ord(s[i])==48:
            if ord(s[i-1]) not in range(48,57):
                return False
            else:
                return True
    return True

def chk_last_num(s):       
    j=len(s)  
    for i in range (len(s)):
        if i==j-1:
            break
        print("s[i]: ",s[i]," :: ",ord(s[i]),"and s[i+1]: ",s[i+1]," :: ",ord(s[i+1]))
        if ord(s[i+1]) in range (65,90):
            print("Oh yeah")
        if 48<=ord(s[i])<=57 and ord(s[i+1]) in range(65,90):
            return False
    return True
        
def chk_let_num(s):
    for _ in range (len(s)):
        if  ord(s[_]) in range(48,57) or ord(s[_]) in range(65,90):
            ...    
        else:
            return False
    return True

def is_valid(s):
    print("Yes 0")
    if chk_let_num(s):
        print("Yes 1")
        if chk_start(s):
            print("Yes 2")
            if chk_len(s):
                print("Yes 3")
                if chk_zero(s):
                    print("Yes 4")
                    if chk_last_num(s):
                        print("Yes 5")
                        return True
                
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

main()