def main():
    print_row(4)
    print("")
    print_colm(3)
    print("\n\n\n")
    print_square(7)
    print("hhhhhhhhhhhhhhhhhhhhhhh")
    print_square2(7)

def print_row(width):
    print("#"*width)

def print_colm(height):
    print("#\n"*height)

def print_square(size):
    for i in range(size):
        print_row(size)

#or
def print_square2(size):
    for i in range(size):
        for j in range(size):
            print("#",end="")
        print()

main()