print("Enter the numbers in  l1:")
l1=[]
for i in range(8):
    i=int(input())
    l1.append(i)

print("Enter the numbers in  l2:")
l2=[]
for i in range(8):
    i=int(input())
    l1.append(i)
   
newlist=l1+l2
print("The numbers in  newlist:",newlist)

newlist.pop()
newlist.pop()
print("The numbers in  newlist after removing last two items:", newlist)

evenlist=[]
oddlist=[]
for i in newlist:
    if i%2==0:
        evenlist.append(i)
    else:
        oddlist.append(i)
print("Evenlist is:",evenlist)
print("Oddlist is:", oddlist)

min=newlist[0]
for n in newlist:
    if n<min:
        min=n
print("So,min num in newlist is ", min)

min=evenlist[0]
for n in evenlist:
    if n<min:
        min=n
print("So,min Even num is ", min)

min=oddlist[0]
for n in oddlist:
    if n<min:
        min=n
print("So,min Odd num is ", min)


