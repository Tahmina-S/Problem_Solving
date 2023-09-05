num=int(input("Enter num: "))

def isPrime(num):
    count=0
    if num==1:
        print("Not Prime")
    for i in range(2,num):
        if num%i==0:
            count=1
    if count==0:
        print("Prime")
    else:
        print("Not Prime")

isPrime(num)                                                                         