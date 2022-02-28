import sys as sys

def Operations(num1: int, num2: int)-> None:
    if int(num2) == 0:          
        print(
            "Sum         "+ str(num1 + num2) +"\n"+
            "Diff        "+ str(num1 - num2) +"\n"+
            "Product     "+ str(num1 * num2) +"\n"+
            "Quotient     ERROR (Div by zero)"+
            "Remainder    ERROR (Modulo by zero)"
            )
    else:            
        print(
            "Sum         "+ str(num1 + num2) +"\n"+
            "Diff        "+ str(num1 - num2) +"\n"+
            "Product     "+ str(num1 * num2) +"\n"+
            "Quotient    "+ str(num1 / num2) +"\n"
            "Remainder   "+ str(num1 % num2) +"\n"
            )
        
    return None

Operations(int(sys.argv[1]),int(sys.argv[2]))