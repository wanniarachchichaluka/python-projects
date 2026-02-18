while True:
    u_date=input("Date: ")
    k=len(u_date)
    a=""
    b=""
    c=""
    count=0
    for i in range(k):
        if count==0 and u_date[i]!='/':
            a=a+u_date[i]
        if u_date[i]=='/':    
            count=count+1
        if count==1 and u_date[i]!='/':
            b=b+u_date[i]
        if count==2 and u_date[i]!='/':
            c=c+u_date[i]

    if 0<int(a)<=12 and int(b)<=31:
        print(f"{c}-{int(a):02}-{int(b):02}")
        break
    else:
        continue