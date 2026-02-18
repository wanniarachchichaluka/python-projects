def func(list):
    list1=list
    list2=[]
    list3=[]
    list4=[]

    i=1
    p=len(list1)-1
    while i<=p:
        x=list1[i]
        list2.append(x[0])
        i=i+2

    i=0
    p=len(list2)-1 #=4
    while i<=p:
        list3.append(ord(list2[i]))
        i=i+1

    i=0
    while len(list1)!=0:
        n=min(list3) 
        if type(list1[i]) == str:
            x=list1[i] 
            y=x[0] 
            if ord(y) == n:
                list4.append(list1[i-1])
                list4.append(x)
                list1.pop(i)
                list1.pop(i-1)
                i=-1
                j=len(list3)-1 
                b=0
                while b<=j: 
                    if list3[b]==n:
                        list3.pop(b)
                        j=j-1
                    b=b+1
        i=i+1 
    return list4


def main():
    list1=[]
    while True:
        try:
            list1.append(input().lower())
        except EOFError:
            break
        except KeyboardInterrupt:
            break

    list2=list1
    list3=[]
    for m in list1:
        count = 0
        for n in list2:
            if m==n and m not in list3:
                count = count + 1
        if m not in list3:
            list3.append(count)
            list3.append(m)

    dic={}
    k=len(list3)
    list3=func(list3)
    for i in range(0,k,2):
        if i!=k-1:
            dic[list3[i+1]]=list3[i]

    for key in dic:
        print(dic[key],key.upper())

main()