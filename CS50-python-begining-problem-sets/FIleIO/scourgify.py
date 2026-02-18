import sys
import csv
humans=[]
humans2=[]
if len(sys.argv)<3:
    print("Too few args")
elif len(sys.argv)>3:
    print("Too many args")
else:
    try:
        if (sys.argv[1]).endswith('.csv') and (sys.argv[2]).endswith('.csv'):
            with open(sys.argv[1],newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    humans.append({"name":row['name'], "house":row['house']})
            for human in humans:
                last, first = human['name'].rstrip().split(",") 
                humans2.append({"first":first, "last":last,"house":human['house']})
            
            import csv

            with open('after.csv', 'w', newline='') as csvfile:
                fieldnames = ['first', 'last', 'house']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                for human in humans2:
                    writer.writerow({'first': human['first'], 'last': human['last'], 'house': human['house']})
        else:
            print("Wrong file type")
    except FileNotFoundError:
        sys.exit("File not found")
