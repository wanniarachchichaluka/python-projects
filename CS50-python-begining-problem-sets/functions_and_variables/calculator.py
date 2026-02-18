#manipulating integers
x=1
y=4
z=x+y
print(z)

x=int(input("what is x? "))
y=int(input("What's y? "))

print(x+y)


####
##manipulating floats
j=float(input("enter a number for j:"))
n=float(input("enter a number for n:"))


#rounding to the nearest integer
z=round((j+n),3)
print(z)
print(f"{z:,}")

######
x=float(input("Enter 1st number: "))
y=float(input("Enter 2nd number: "))

z=x/y
print(z)
k=round(z,3)
print(k)
print(f"{k:.2f}")