def total(a,b,c):
    return (a*17+b)*29+c

coins = (100,50,25)
print(total(*coins), "c") # will unpack the coins into 3 seperate arguments