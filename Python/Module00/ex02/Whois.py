import sys as sys

class num:

    def __init__(self,number) -> None:
        if len(number) == 1: # check if there is only 1 parameter
            if number[0].isnumeric(): # check if the parameter is numeric
                self.number = int(number[0])
            else:
                print('ERROR')
        else:
            print('ERROR')
    
    def who(self):
        if self.number == 0:
            print("I'm Zero.")
        elif self.number%2 == 0: # % is equivalent to modulo (the rest of the division)
            print("I'm Even.")
        else:
            print("I'm Odd.")
        


def main():
    test = num(sys.argv[1:])
    if hasattr(test, 'number'): # Check if there is an attribue number in test
        test.who()

main()
