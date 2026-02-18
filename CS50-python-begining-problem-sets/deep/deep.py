answer=input("What is the answer to the Great Question of Life: ")
match answer.strip().lower():
    case "forty-two" | "forty two" | "42":
        print("Yes")
    case _:
        print("No")

        