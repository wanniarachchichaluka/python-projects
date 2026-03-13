#running: mypy .\meow_typeHint.py
def meow(n: int) -> None: #to hint what the return value is use ->
    for _ in range(n):
        print("meow")

number: int = int(input("Number: "))
meows: str= meow(number)
print(meows)

#to see the solution for mypy error see the meow_typeHint2.py
