n=int(input("Enter Year:"))

if n%4==0:
    if n%100!=0:
        print("LeapYear")
elif n%400==0:
    print("LeapYear")
else:
    print("Non-LeapYear")