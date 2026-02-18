"""
Day 1.1 : 30/11/2025 : 6.30pm
Day 1.2 : 6/12/2025 : 7.24am
"""

#Asking user for their name
user_name=input("Hello man, what is your name: ")

#Saying hello to the user
print(f"1-Hello, {user_name}")

#several methods to do the same above
print("2-Hello, "+user_name)
print("3-Hello,",user_name)

#starting a conversation
print("So,")

#asking the user for his age
print(user_name,"What is your age: ")
user_age=input()
print("So",user_name + "'s age is: "+user_age)

print(user_age)

######################
##################
print("Hello, ",end="")
print("how are you") 

print("Hey look, what "," fuck ",sep="the",end=" Happend")

print('\nHello, "friend"')
print("Yes, \"friend\"")

name="Chaluka"
print(f"Hello, {name}")
 
#Removing white spaces of a string of a user input.
#but still remains the spaces in between
age=input("What is your age: ")
age=age.strip()
print("Your age is:",age)

#capitalizing first letter of user input
colour=input("What is your colour:")
colour=colour.capitalize()
print("You really like "+colour)
#capitalizing the 1st letter of each word
colour=colour.title()
print("Did I hear ",colour)

#doing each every above manipulation together
address=input("What is your address:")
address=address.strip().title()
print("So you're currently living in: "+address)

#all in one line
full_name=input("what is your full name:").title().strip()
print(f"So officially you're: Mr {full_name}")

#######
#splitting user's name into first name & last name
full_name=input("what is your full name:").title().strip()
first_name,last_name=full_name.split(" ")
print("Hi,",first_name+"?????",last_name)


