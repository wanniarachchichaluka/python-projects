import sys
import csv
from PIL import Image,ImageOps
humans=[]
humans2=[]
image1_1=None
image2_1=None

if len(sys.argv)<3:
    sys.exit("Too few args")
elif len(sys.argv)>3:
    sys.exit("Too many args")
else:
    x,y=sys.argv[1].split(".")
    z,j=sys.argv[2].split(".")
    try:
        if str.lower(y) == 'jpg' or str.lower(y) == 'jpeg' or str.lower(y) == 'png':
            if str.lower(j) == 'jpg' or str.lower(j) == 'jpeg' or str.lower(j) == 'png':
                if str.lower(y)==str.lower(j):
                        with Image.open(sys.argv[2]) as image2:    
                            size2 = image2.size
                            print(size2)
                            image2_1=ImageOps.fit(image2,size2)
                        with Image.open(sys.argv[1]) as image1:
                            image1_1=ImageOps.fit(image1,size2)
                        image1_1.paste(image2_1,image2_1)
                        image1_1.save("afterbla.png")
                else:
                    sys.exit("extensions doesn't match")
            else:
                sys.exit("Wrong extension type2")
        else:
            sys.exit("Wrong extension type")
    except FileNotFoundError:
        sys.exit("given files does not exist")
    

 
