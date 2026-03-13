import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")

parser.add_argument("-n", default=1, help="Number of times to meow", type=int)
args = parser.parse_args() #parse_args() automatically look at sys.argv for me
#args is an object return by parse_args() function
for _ in range(int(args.n)):
    print("meow")

