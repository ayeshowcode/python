x=0
match x:
    case 0:
        print("x is 0")
    case 1:
        print("x is 1")
    case 2:
        print("x is 2")
    case 3:
        print("x is 3")
    case _: #default case
        print("greater than 3")
    
    
    
y=int(input("Enter a number: "))
match y:
    case 0:
        print("y is 0")
    case 1:
        print("y is 1")
    case 2:
        print("y is 2")
    case 3:
        print("y is 3")
    case _ if(x==9): #default case
        print("y is 9")
    case _ if(x==10): #default case
        print("y is 10")
    case _:
        print("greater than 3 and not 9 or 10")
    