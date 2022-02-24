class Evaluator:

    def __init__(self) -> None:
        pass

    def zip_evaluate(words,coefs):
        if len(words) != len(coefs): # Check the length of the two lists
            return -1

        else :  
            r = 0
            for (word,value) in zip(words,coefs): # read at the same time the two list with the same index
                r = r + len(word) * value
            return r

    def enumerate_evaluate(words,coefs):
        if len(words) != len(coefs):  # Check the length of the two lists
            return -1

        else :  
            temp : list[int] = [] # list of length of all words
            r = 0
            for word in words:
                temp.append(len(word))
            for i,value in enumerate(coefs): # Read the list and make an enumaration from 0 ... len(list)
                r = r + temp[i] * value

            return r

def main():
    print(Evaluator.zip_evaluate(["Le", "Lorem", "Ipsum", "est", "simple"],[1.0, 2.0, 1.0, 4.0, 0.5]))
    print(Evaluator.enumerate_evaluate(["Le", "Lorem", "Ipsum", "est", "simple"],[1.0, 2.0, 1.0, 4.0, 0.5]))

main()