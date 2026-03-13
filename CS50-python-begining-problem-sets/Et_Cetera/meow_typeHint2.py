#running: mypy .\meow_typeHint.py
def meow(n: int) -> str: #to hint what the return value is use ->
    return "meow\n" * n

number: int = int(input("Number: "))
meows: str= meow(number)
print(meows, end="")