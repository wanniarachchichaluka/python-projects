class Vault:
    def __init__(self, g=0, s=0, k=0):
        self.g=g
        self.s=s
        self.k=k
    
    def __str__(self):
        return f"{self.g} g's, {self.s} s's, {self.k} k's"

potter = Vault(100,50,25)
print(potter)
        
cat = Vault(1,2,3)
print(cat)

g = potter.g + cat.g
s = potter.s + cat.s
k = potter.k + cat.k
#we can do the same thing above using operator overloading
#refer the vault1.py

total = Vault(g,s,k)
print(total)