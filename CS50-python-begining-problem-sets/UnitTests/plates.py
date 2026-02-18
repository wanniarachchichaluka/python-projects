def is_valid(s):
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
            if ord(s[i+1]) in range (65,90):
                ...
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
    if chk_let_num(s):
        if chk_start(s):
            if chk_len(s):
                if chk_zero(s):
                    if chk_last_num(s):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
                
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

if __name__=="__main__":
    main()