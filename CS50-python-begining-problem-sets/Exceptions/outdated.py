while True:
    try:
        u_date=input("Date: ")
        list1=[
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
        ]
        k=len(u_date)
        a=""
        b=""
        c=""
        set=0
        for i in range(k):
            if u_date[i]=='/':
                set=1
        if set==0:
            count=0
            for i in range(k):
                if count==0 and u_date[i]!=' ':
                    a=a+u_date[i]
                if u_date[i]==' ':    
                    count=count+1
                    continue
                if count==1 and u_date[i]!=',':
                    b=b+u_date[i]
                if u_date[i]==',':
                    count=count+1
                if count==3:
                    c=c+u_date[i]

            k=len(list1)
            i=0
            try:
                if int(b)<=31:
                    for i in range(k):
                        if list1[i]==a and count==3:
                            print(f"{c}-{(i+1):02}-{int(b):02}")
                            set=2
                        i=i+1
                    if set==2:
                        break
                    continue
                else:
                    continue
            except ValueError:
                continue
        if set==1:
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
                print(f"{int(c)}-{int(a):02}-{int(b):02}",sep="")
                break
            else:
                continue
    except ValueError:
        continue
