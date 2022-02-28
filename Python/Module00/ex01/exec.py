import sys as sys

class Reverse:

    def __init__(self, words= list):
       self.words  = words # table of all words in the execution
       self.string = ''  #  The string to reverse
    
       if len(self.words) > 1: # Concatenate all words when there is more than 1
           for word in self.words:
               if self.string=='':
                   self.string = self.string + word 
               else:
                    self.string = self.string + ' ' + word
       elif len(self.words) == 1: 
           self.string =  words[0] 
       else:
           self.string = input()


    def reverse_func(self):
        temp = ''
        i = len(self.string)
        while i > 0:
            if self.string[i-1].isalpha(): # Detecte if the character is alphabetic
                if self.string[i-1].islower(): # Detecte if the character is lower
                    temp = temp + self.string[i-1].upper() 
                    i=i-1
                elif self.string[i-1].isupper(): # Detecte if the character is upper
                    temp = temp + self.string[i-1].lower()
                    i=i-1
            else: 
                temp = temp + self.string[i-1]
                i=i-1
        
        self.string = temp
            



def main():
    w = Reverse(sys.argv[1:])
    w.reverse_func()
    print(w.string)



main()