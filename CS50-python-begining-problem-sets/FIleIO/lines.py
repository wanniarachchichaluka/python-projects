import sys
count1=0
count2=0
count3=0
if len(sys.argv)<2:
    print("Too few args")
elif len(sys.argv)>2:
    print("Too many args")
else:
    try:
        if (sys.argv[1]).endswith('.py'):
            with open(sys.argv[1]) as file:
                for line in file:
                    if line.rstrip().startswith('#'):
                        count1=count1+1
                    elif len(line.rstrip())==0:
                        count2=count2+1
                    else:
                        print(len(line.rstrip()))
                        count3=count3+1
        else:
            print("Wrong file type")
    except FileNotFoundError:
        sys.exit("File not found")

print("Nu of commented lines: ",count1)
print("Nu of new lines: ",count2)
print("Nu of effective lines: ",count3)