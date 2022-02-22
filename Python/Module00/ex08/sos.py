import sys as sys

class sos:

    def __init__(self,words) -> None:
        self.morse = {
            "A" :   ".-",
            "B" :   "-…",
            "C" :   "-.-.",
            "D" :   "-..",
            "E" :   ".",
            "F" :   "..-.",
            "G" :   "- -.",
            "H" :   "….",
            "I" :  "..",
            "J" :  ".- - -  ",
            "K" :   "-.-",
            "L" :   ".-..",
            "M" : "- -",
            "N" :   "-.",
            "O" :  "- - -",
            "P" :   ".- -.",
            "Q" :  "- -.-",
            "R" :   ".-.",
            "S" :  "…",
            "T" :   " -",
            "U" :   "..-",
            "V" :  "…-",
            "W" :  ".- -",
            "X" :  "-..-",
            "Y" :  "-.- -",
            "Z" :  "- -..",
            " " :  ".",
            "0" :  "-----",
            "1" :  ".----",
            "2" :  "..---",
            "3" :  "...--",
            "4" :  "....-",
            "5" :  ".....",
            "6" :  "-....",
            "7" :  "--...",
            "8" :  "---..",
            "9" :  "----."
            }
        if len(words) == 1:
            self.words = words[0]
            self.in_morse()

        elif len(words) > 1:
            self.words = ' '.join(words)
            print(self.words)
            self.in_morse()
        
        else:
            print("ERROR")

    def in_morse(self):
        text_morse = ""
        for c in self.words:
            for m in self.morse:
                if c.isalpha:
                    if c.upper() == m:
                        text_morse = text_morse + self.morse[m]
                
                elif c== m:
                    text_morse = text_morse + self.morse[m]
        
        print(text_morse)


def main():
    test = sos(sys.argv[1:])

main()