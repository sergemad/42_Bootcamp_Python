import sys as sys

class operations:

    def __init__(self, numbers) -> None:
        
        if len(numbers) == 2: #check if the right number of arguments is in execution
            self.num1, self.num2 = numbers[0], numbers[1]
            if self.num1.isnumeric() and self.num2.isnumeric(): # check if arguments are numeric
                if int(self.num2) == 0:                           #  if number2 is zero
                    print('Sum:        '+str(int(self.num1)+int(self.num2))+'\n'+
                          'Difference: '+str(int(self.num1)-int(self.num2))+'\n'+
                          'Product:    '+str(int(self.num1)*int(self.num2))+'\n'+
                          'Quotient:   ERROR (Div by zero)\n'+
                          'Remainder:  ERROR (Modulo by zero)\n')
                else:
                    print('Sum:        '+str(int(self.num1)+int(self.num2))+'\n'+
                          'Difference: '+str(int(self.num1)-int(self.num2))+'\n'+
                          'Product:    '+str(int(self.num1)*int(self.num2))+'\n'+
                          'Quotient:   '+str(int(self.num1)/int(self.num2))+'\n'+
                          'Remainder:  '+str(int(self.num1)%int(self.num2)))
            else:
                print('InputError: Only numbers \n\n Usage: python operations.py <number1> <number2>\n Exemple:\n python operations.py 10 3')

        elif len(numbers) < 2: 
            print('InputError: not enought arguments \n\n Usage: python operations.py <number1> <number2>\n Exemple:\n python operations.py 10 3')

        else:
            print('InputError: too many arguments \n\n Usage: python operations.py <number1> <number2>\n Exemple:\n python operations.py 10 3')

def main():
    o = operations(sys.argv[1:])

main()
