import sys as sys

def filterwords(words: str ,n: int)-> None:
    wordfilter : list[str] = []
    char =[
        ",",
        ".",
        ";",
        ":",
        "?",
        "!",
        "(",
        ")",
        "/"
        ]
    texte = words
    for c in char:
        texte = texte.replace(c,"")
    splited = texte.split()
    for s in splited:
        if len(s) > n:
            wordfilter.append(s)
    
    print(wordfilter)
        

def main():
    filterwords(sys.argv[1],int(sys.argv[2]))

main()
