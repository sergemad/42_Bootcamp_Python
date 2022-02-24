import random

def generator(text, sep=" ", option=None) -> list:
    '''Splits the text according to sep value and yield the substrings.
       option precise if a action is performed to the substrings before it is yielded.
    '''
    text_splited = text.split(sep)
    temp : list[str] = []
    if  option == "shuffles":
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

    elif option == "unique":
        for st in text_splited:
            if not(st in temp):
                temp.append(st)
        
        text_splited = temp

    elif option == "ordered":
        text_splited.sort()

    return text_splited 


def main():
    t = generator("Salut je fais juste un teste un un", " ","shuffles")
    print(t)

main()
