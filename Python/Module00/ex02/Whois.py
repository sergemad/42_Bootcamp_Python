import sys as sys

class Num:

    def __init__(self, number= int):   
        self.number = int(number[0])
    
    def who(self):
        if self.number == 0:
            print("I'm Zero.")
        elif self.number%2 == 0: 
            print("I'm Even.")
        else:
            print("I'm Odd.")
        


def main():
    test = Num(sys.argv[1])
    if hasattr(test, 'number'): # Check if there is an attribute number in test
        test.who()

main()
