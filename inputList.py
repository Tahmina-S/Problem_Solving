num=int(input("How many items in list?"))
print("List contains",num, "items")
newlist=[]
evenlist=[]
oddlist=[]

for i in range(num):
    i=int(input())
    newlist.append(i)
for i in newlist:
    if i%2==0:
        evenlist.append(i)
    else:
        oddlist.append(i)
print("newlist is:",newlist)
print("Evenlist is:",evenlist)
print("Oddlist is:", oddlist)

Max=newlist[0]
for n in newlist:
    if n>Max:
        Max=n
print("So,Max num is ", Max)

Max=evenlist[0]
for n in evenlist:
    if n>Max:
        Max=n
print("So,Max Even num is ", Max)

Max=oddlist[0]
for n in oddlist:
    if n>Max:
        Max=n
print("So,Max Odd num is ", Max)

print("Largest num from Newlist using :", max(newlist))
print("Largest num from Evenlist using :", max(evenlist))
print("Largest num from Oddlist using :", max(oddlist))

