list1=["A","c","k","b"]
list2=["r","g","y","m"]

list1.extend(list2)

for i in list1:
    for n in i:
        if "A" in i or "r" in i:
            print(n)

new=[]
for i in list1:
    if "k" in i:
        new.append(i)
print(new)


num=int(input("How many items in list?"))
print("List contains",num, "items")

newlist=[]

for i in range(num):
    i=int(input())
    newlist.append(i)

evenlist=[]
oddlist=[]

for i in newlist:
    if i%2==0:
        evenlist.append(i)
    else:
        oddlist.append(i)

print("Evenlist is:",evenlist)
print("Evenlist is:", oddlist)



