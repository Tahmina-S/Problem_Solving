a,b,c,d=int(input("Enter A: ")),int(input("Enter B: ")),int(input("Enter C: ")),int(input("Enter D: "))

if a>b:
    if a>c:
        if  a>d:
            print("A  is Greater.")        
        else:
            print("D  is Greater.")       
    else:
        if  c>d:
            print("C  is Greater.")        
        else:
            print("D  is Greater.") 
      
else:
    if b>c:
        if  b>d:
            print("B  is Greater.")        
        else: 
             print("D  is Greater.")
    else:
        if  c>d:
            print("C  is Greater.")        
        else:
            print("D  is Greater.") 
       


