import sys as sys

class Text:

    def __init__(self,text= str): 
        self.text = ''

        if len(text) == 1: 
            self.text = text[0]
        elif len(text) == 0:  
            self.text = input()
        else:
            print('ERROR')
        
    def text_analyzer(self):  
        if self.text != '':
            length = len(self.text)
            upper, lower, space, punctuation = 0,0,0,0
            for char in self.text:
                if char.isalpha():  
                    if char.islower():
                        lower = lower + 1
                    else:
                        upper = upper + 1
                elif char.isspace(): 
                    space = space + 1
                elif char.isnumeric(): 
                    pass
                else: 
                    punctuation = punctuation + 1
            
            print('The text contains ' +str(length)+ ' characters:')
            print('- '+ str(upper) +' upper letters')
            print('- '+ str(lower) +' lower letters')
            print('- '+ str(punctuation) +' punctuation marks')
            print('- '+ str(space) +' spaces')
        

def main():
    t = Text(sys.argv[1:])
    t.text_analyzer()

main()

