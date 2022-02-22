import sys as sys

class text:

    def __init__(self,text) -> None:   # Constructor of classe
        self.text = ''

        if len(text) == 1: 
            self.text = text[0]
        elif len(text) == 0:  # If there is no parameter, make an input for user
            self.text = input()
        else:
            print('ERROR')
        
    def text_analyzer(self):  
        if self.text != '':
            length = len(self.text)
            upper, lower, space, punctuation = 0,0,0,0
            for char in self.text:
                if char.isalpha():  # test if the character is alphabetic 
                    if char.islower(): # test if  the character is lower case
                        lower = lower + 1
                    else:
                        upper = upper + 1
                elif char.isspace(): # check if the character is a space
                    space = space + 1
                elif char.isnumeric(): # Check if the character is numeric
                    pass
                else: 
                    punctuation = punctuation + 1
            
            print('The text contains ' +str(length)+ ' characters:')
            print('- '+ str(upper) +' upper letters')
            print('- '+ str(lower) +' lower letters')
            print('- '+ str(punctuation) +' punctuation marks')
            print('- '+ str(space) +' spaces')
        

def main():
    t = text(sys.argv[1:])
    t.text_analyzer()

main()

