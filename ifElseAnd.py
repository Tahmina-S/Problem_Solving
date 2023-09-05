a,b,c,d=int(input("Enter A: ")),int(input("Enter B: ")),int(input("Enter C: ")),int(input("Enter D: "))
if a>b and a>c and a>d:
    print("A is Greatest.")
elif b>a and b>c and b>d:
    print("B is Greatest.")
elif c>a and c>b and c>d:
    print("C is Greatest.")
else:
    print("D is Greatest.")
    