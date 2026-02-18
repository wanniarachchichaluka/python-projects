list1=[1, 'orange', 1, 'apple', 3, 'pine apple']
list2=['o','a','p']
list3=[111,97,112]

i=0

k=len(list1)-1 #=5
list4=[]
while i<=k:
    n=min(list3) #n=111
    if type(list1[i]) == str:
        x=list1[i] #=apple
        y=x[0] #=a
        if ord(y) == n:
            list4.append(x)
            list1.pop(i)
            list1.pop(i-1)
            k=k-1 #=4
            j=len(list3)-1
            b=0
            while b<=j:
                if list3[b]==n:
                    list3.pop(b)
                    j=j-1
    i=i+1 #=4

    [1,'orange',3,'pine apple']
    [111,112]
