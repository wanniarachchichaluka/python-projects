def total(a,b,c):
    return (a*17+b)*29+c

coins = {"a":100, "b":50, "c":25}

#print(total(a=100,b=50,c=25), "c") 
#print(total(coins["a"],coins["b"],coins["c"]),"c")

print(total(**coins),"c")#two ** for unpacking a dictionary. because keys and values

