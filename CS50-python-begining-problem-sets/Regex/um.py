import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    matches6 = re.findall(r'\bum[.,? ]*', str.lower(s)+" ")
    return len(matches6)


if __name__ == "__main__":
    main()