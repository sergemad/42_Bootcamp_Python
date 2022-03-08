import numpy as np
from typing import Literal

Bin = Literal[0,1]

class ScrapBooker:

    def __init__(self) -> None:
        pass

    def crop(self, array: np, dimension: tuple, position : tuple = (0,0) ) -> np:
        array = array[position[0]:]
        temp : list = []
        dim : int = 0
        for j in range(0,array.shape[1]):
            if j < position[1] or dim >= dimension[1]:
                temp.append(j)
            else: 
                dim = dim + 1
        array = np.delete(array, temp, 1)
        array = array[0:dimension[0]]
        return array
    
    def thin(self, array: np, n: int, axis : Bin) -> np:

        if axis == 0:
            shape_id : int = 1
        elif axis == 1:
            shape_id : int = 0
        
        n_ : int = 1
        temp : list[int] = []
        for i in range(0,array.shape[shape_id]):
            if n == n_:
                temp.append(i)
                n_ = 1
            else:
                n_ = n_ + 1
        array = np.delete(array, temp, shape_id)

        return array
    
    def juxtapose(self, array : np, n : int, axis : Bin) -> np:
        arr = array.copy()
        for i in range(1,n):
            array = np.concatenate((array, arr), axis)
        return array

    def mosaic(self, array : np, dimension : tuple ) -> np:
        grid : list = []
        line_grid : list = []
        for i in range(0,dimension[0]):
            for j in range(0,dimension[1]):
                line_grid.append(array)
            grid.append(line_grid)
            line_grid : list = []
        return np.array(grid)


arr = np.array([[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6]])
t = ScrapBooker()
#print(t.crop(arr,(2,7),(1,1)))
#print(t.thin(arr,3,1))
#print(t.juxtapose(arr, 3, 1))
#print(t.mosaic(arr,(3,3)))
