import numpy as np

class NumPyCreator:

    def __init__(self) -> None:
        pass

    def from_list(self, lst : list) -> list: 
        return np.array(lst)

    def from_tuple(self,tpl : tuple) -> list:
        npy = []
        for value in tpl:
            npy.append(value)
        return np.array(npy)

    def from_iterable(self, r) -> list:
        npy = []
        for value in r:
            npy.append(value)
        return np.array(npy)
    
    def random(self, shape : tuple[int])-> list:
        npy = []
        for i in range(0,shape[0]):
            npy.append([0])
            for j in range(1,shape[1]):
                npy[i].append(0)
        
        return np.array(npy)
    
    def identity(self, ident : int) -> list:
        npy =[]
        for i in range(0,ident):
            npy.append([])
            for j in range(0,ident):
                if i == j:
                    npy[i].append(1)
                else:
                    npy[i].append(0)
                
        return np.array(npy)


shape = (3,5)
test = NumPyCreator()
print(
    test.random(shape),
    test.from_iterable(range(5)),
    test.from_list([[1,2,3],[1,2,3]]),
    test.from_tuple(("a","b","c")),
    test.identity(5),
    sep='\n'
    )