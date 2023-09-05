thislist=["a","b","c"]
list1=["d","e","f"]

list1.append("bashar")
list1.extend(thislist)
list1.insert(2, "Public")
thislist.extend(list1)

print(thislist)
print(list1)



