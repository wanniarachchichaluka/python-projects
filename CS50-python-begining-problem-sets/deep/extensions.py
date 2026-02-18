list1=['.gif','.jpg','.jpeg','.png','.pdf','.txt','.zip']

y=input("File name: ")
x=str.lower(y)
count=0
for i in list1:
    if x.endswith(i):
        count = 1
        z=i[1:]
        if i=='.jpg' or i=='.jpeg':
            z='jpeg'
if count==1:
    print(f"image/{z}")
else:
    print("application/octet-stream")