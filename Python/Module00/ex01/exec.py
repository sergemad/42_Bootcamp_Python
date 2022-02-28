import sys as sys

def concat_words(words: list[str])-> str:
    string : str = ''  #  The string to reverse
    
    if len(words) > 1: # Concatenate all words when there is more than 1
        for word in words:
            if string=='':
                string = string + word 

            else:
                string = string + ' ' + word

    else:
        string = input()
    
    return string


def reverse_func(words: list[str])-> str:
    string = concat_words(words)
    temp : str = ''
    i = len(string)
    while i > 0:
        if string[i-1].isalpha(): # Detecte if the character is alphabetic
            if string[i-1].islower(): # Detecte if the character is lower
                temp = temp + string[i-1].upper() 
                i=i-1
            elif string[i-1].isupper(): # Detecte if the character is upper
                temp = temp + string[i-1].lower()
                i=i-1
        else: 
            temp = temp + string[i-1]
            i=i-1
    
    string = temp
    return string
            



def main():
    w = reverse_func(sys.argv[1:])
    print(w)



main()