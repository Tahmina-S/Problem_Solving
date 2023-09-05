n=int(input("Inputs: "))
mylist=[]
for i in range(1,n+1):
    i =int(input("Enter input {} : ".format(i)))
    mylist.append(i)

def Average(l1):
    sum=0    
    for i in l1:
        sum=sum+i
    print("Average is: ", sum/n)

Average(mylist)