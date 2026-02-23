import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        matches6 = re.search(r'.+(src="http.+youtube[^"]+)',s)
        matches7 = re.search(r'.+/([^/]+)$',matches6.group(1))
        return "https://youtu.be/" + matches7.group(1)
    except AttributeError:
        pass

if __name__ == "__main__":
    main()