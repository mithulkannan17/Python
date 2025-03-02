# match case statements

x = int(input("Enter the value of X: "))

match x:
    case 0:
        print("x is zero")
        
    case _ if x < 0:
        print("x is Negative Number")
        
    case _ if x > 0:
        print("x is Positive Number")
        
    case _:
        print("Invalid")
        
    
        