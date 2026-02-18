name=input("What's ur name: ")

match name:
    case "Harry" | "Herm" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slyth")
    case _:
        print("Who?")

if name=="Herm" or "Harry":
    print("Griff")
