from validator_collection import validators, checkers, errors
import sys
j=input("What's your email address? ")

try:
    email_address = validators.email(j)
    print("Valid")
except errors.EmptyValueError:
    print("Invalid")
except errors.InvalidEmailError:
    print("Invalid")
except ValueError:
    print("Invalid")