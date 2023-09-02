thislist = ["","","",""]
print(thislist)
thislist[0]='a'
thislist[1]='b'
thislist[2]='c'
thislist[3]='d'
print(thislist)
thislist.pop(3)
print(thislist)

list1=['a','b','c']
list2=['d','e','f']

list1.append('p')
print(list1)
list2.extend(list1)
print(list2)
list2.insert(2,"z")
print(list2)
list2.remove('a')
print(list2)
list2.pop()
print(list2)
list2.pop(3)
print(list2)
