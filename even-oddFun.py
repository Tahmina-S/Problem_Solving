print("Enter the numbers in  newlist:")
newlist=[]
for i in range(8):
    i=int(input())
    newlist.append(i)
    
evenlist=[]
oddlist=[]

def even_odd(evenlist,oddlist):
    for i in newlist:
        if i%2==0:
            evenlist.append(i)
        else:
            oddlist.append(i)
    print("Evenlist is:",evenlist)
    print("Oddlist is:", oddlist)

# def MinNew():
#     min=newlist[0]
#     for n in newlist:
#         if n<min:
#             min=n
#     print("So,min num in newlist is ", min)

def MaxEven(evenlist):
    max=evenlist[0]
    for n in evenlist:
        if n>max:
            max=n
    print("So,max Even num is ", max)

def MaxOdd(oddlist):
    max=oddlist[0]
    for n in oddlist:
        if n>max:
            max=n
    print("So,max Odd num is ", max)

def MinEven(evenlist):
    min=evenlist[0]
    for n in evenlist:
        if n<min:
            min=n
    print("So,min Even num is ", min)

def MinOdd(oddlist):
    min=oddlist[0]
    for n in oddlist:
        if n<min:
            min=n
    print("So,min Odd num is ", min)

even_odd(newlist)
MaxEven(newlist)
MaxOdd(newlist)
MinEven(newlist)
MinOdd(newlist)