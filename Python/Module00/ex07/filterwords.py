import sys as sys

class filterwords:

    def __init__(self, words) -> None:
        if len(words) == 2: 
            if not(words[0].isnumeric()) and words[1].isnumeric():
                self.words = words[0]
                self.n = int(words[1])
                self.wordfilter : list[str] = []
                self.fsplit()

            else:
                print("ERROR")

        else:
            print("ERROR")


    def fsplit(self):
        char =[",",".",";",":","?","!","(",")","/"]
        texte = self.words
        for c in char:
            texte = texte.replace(c,"")

        splited = texte.split()

        for s in splited:
            if len(s) > self.n:
                self.wordfilter.append(s)
        
        print(self.wordfilter)
        

def main():
    test = filterwords(sys.argv[1:])

main()
