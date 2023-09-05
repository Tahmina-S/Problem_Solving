DaffodilBugs=["Pritom ","Shazid ","Fakrul ","Tahmina ","Milon "]
DIPTIPydantic=["Joy ","Ahaduzzaman","Rupa ","Bejoy ","Lokman "]
Pythoneers=["Tahmeed ","Abrar ","Erfanul ","Tasnim ","Sumiya "]
JSRMUnity=["Jilan ","Mishan ","Sima ","RASHEL "]
Hungrybirds=["Ajoy ","Rakib ","Hasib ","Mehedi ","Farhan "]

teamlist=[]

teamlist=[DaffodilBugs,DIPTIPydantic,Pythoneers,JSRMUnity,Hungrybirds]
new=[]

teamlist.extend(DaffodilBugs)
print(teamlist)
teamlist.extend(DIPTIPydantic)
print(teamlist)
teamlist.extend(Pythoneers)
print(teamlist)
teamlist.extend(JSRMUnity)
print(teamlist)
teamlist.extend(Hungrybirds)
print(teamlist)


for i in DaffodilBugs,DIPTIPydantic,Pythoneers,JSRMUnity,Hungrybirds:
      teamlist.extend(i)
print (teamlist)

newlist=[]
for i in teamlist:
   for j in i:
     newlist.append(j)
print (newlist)

for i in range(len(teamlist)):
    for j in teamlist[i]:
        if j=="Jilan " or j=="Mishan ":
            continue
        newlist.append(j)
        print(j)
print (newlist)



for i in teamlist:
  new.append(i)
  if i==JSRMUnity:
    break
print(new)

for i in teamlist:   
   if i==JSRMUnity:
     continue
   new.append(i)
print(new)














