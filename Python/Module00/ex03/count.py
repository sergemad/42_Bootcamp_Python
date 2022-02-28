import sys as sys
    
def text_analyzer(text: str)-> None:
    if text != '':
        length : int = len(text)
        upper, lower, space, punctuation = 0,0,0,0
        for char in text:
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
    text_analyzer(sys.argv[1])

main()

