import sys as sys

class Operations:

    def __init__(self, numbers) -> None:
        
        if len(numbers) == 2: #check if the right number of arguments is in execution
            self.num1, self.num2 = numbers[0], numbers[1]
            if self.num1.isnumeric() and self.num2.isnumeric(): # check if arguments are numeric
                if int(self.num2) == 0:                           #  if number2 is zero
                    print(f"Sum:        {int(self.num1) + int(self.num2)}" "\n"
                          f"Difference: {int(self.num1) - int(self.num2)}" "\n"
                          f"Product:    {int(self.num1) * int(self.num2)}" "\n"
                          'Quotient:   ERROR (Div by zero)\n'+
                          'Remainder:  ERROR (Modulo by zero)\n')
                else:
                    print(
                        f"Sum:        {int(self.num1) + int(self.num2)}" "\n"
                        f"Difference: {int(self.num1) - int(self.num2)}" "\n"
                        f"Product:    {int(self.num1) * int(self.num2)}" "\n"
                        f"Quotient:   ERROR (Div by zero)"               "\n"
                        f"Remainder:  ERROR (Modulo by zero)"            "\n"
                    )
            else:
                print('InputError: Only numbers \n\n Usage: python operations.py <number1> <number2>\n Exemple:\n python operations.py 10 3')

        elif len(numbers) < 2: 
            print('InputError: not enought arguments \n\n Usage: python operations.py <number1> <number2>\n Exemple:\n python operations.py 10 3')

        else:
            print('InputError: too many arguments \n\n Usage: python operations.py <number1> <number2>\n Exemple:\n python operations.py 10 3')

def main():
    o = Operations(sys.argv[1:])

main()
