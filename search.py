def sum(l1):
    sum=0    
    for i in l1:
        sum=sum+i
    print("Sum is: ", sum)

def searching(l1):
    search=int(input("Which num do you want to find: "))
    found=0
    foundlist=[]

    for i in range(len(l1)):
        if l1[i]==search:
            found=found+1
            foundlist.append(i)
    if found==0:
        print("Not found")
    else:
        print("{} Num item found {} times".format(search,found))
    print("foundlist index : ",foundlist)

def even_odd(mylist):
    evenlist=[]
    oddlist=[]
    for i in mylist:
        if i%2==0:
            evenlist.append(i)
        else:
            oddlist.append(i)
    print("Evenlist is:",evenlist)
    print("Oddlist is:", oddlist)


n=int(input("Input items : "))
mylist=[]
for i in range(1,n+1):
    i =int(input("Enter {} num itmem: ".format(i)))
    mylist.append(i)

print(mylist)
sum(mylist)
searching(mylist)
even_odd(mylist)