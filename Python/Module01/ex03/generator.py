import random
from typing import Literal

Options = Literal["shuffle", "ordered", "unique"]

def randomize(text_splited : list[str]):
    temp : list[str] = []
    temp_int : list[int] = []
    for st in text_splited:
        i = random.randint(0,len(text_splited)-1)
        while i in temp_int:
            i = random.randint(0,len(text_splited)-1)  
        
        temp_int.append(i)
        temp.append(st)
    
    id = 0
    for rand_i in temp_int:
        temp[rand_i] = text_splited[id]
        id = id + 1
    
    text_splited = temp
    return text_splited

def generator(text: str, sep: str =" ", option: Options = "ordered") -> list:
    '''
    Splits the text according to sep value and yield the substrings.
    option precise if a action is performed to the substrings before it is yielded.
    '''
    text_splited = text.split(sep)
    if  option == "shuffles":
        text_splited = randomize(text_splited)

    elif option == "unique":
        text_splited = list(set(text_splited))

    elif option == "ordered":
        text_splited.sort()

    for i in  text_splited:
        yield i


def main():
    for w in generator("Salut je fais juste un teste un un", " ","shuffles"):
        print(w)

main()
