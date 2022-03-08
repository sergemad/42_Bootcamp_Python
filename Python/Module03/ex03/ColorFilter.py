import numpy as np
import matplotlib.pyplot as plt
from ImageProcessor import ImageProcessor
from typing import Literal

Filter = Literal['mean', 'weighted', 'm', 'w']

class ColorFilter:

    def __init__(self) -> None:
        pass

    def invert(self, array : np) -> np:
        invert_im = (255-array)
        return invert_im
    
    def to_blue(self, array : np) -> np:
        im_blue = np.zeros(array.shape,dtype=int)
        for i in range(0,array.shape[0]):
            for j in range(0,array.shape[1]):
                im_blue[i][j][2] = int(array[i][j][2])
        return im_blue

    def to_green(self, array : np) -> np:
        im_green = array*[0,1,0]
        return im_green
    
    def to_red(self, array : np) -> np:
        im_red = array - self.to_blue(array)
        im_red = im_red - self.to_green(array)
        return im_red
    
    def to_celluloid(self, array : np) :
        pass

    def to_grayscale(self, array : np , filter : Filter )-> np:
        gray_im : list = []
        for i in range(0,array.shape[0]):
            gray_im.append([])
            for j in range(0,array.shape[1]):
                if filter == 'mean' or filter == 'm':
                    gray_im[i].append([
                        ( np.sum(array[i][j]) / 3 ) / 255
                    ])
                else:
                    gray_im[i].append([
                        np.sum( 
                            array[i][j] * 
                            np.array([0.299,0.587,0.114])
                        )
                    ])
        gray_im = np.array(gray_im)
        plt.imshow(gray_im)
        plt.show()

test = ImageProcessor()
arr = test.load("test.jpg")
cfil = ColorFilter()
cfil.to_grayscale(arr,'w')
