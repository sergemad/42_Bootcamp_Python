import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np

class ImageProcessor:

    def __init__(self) -> None:
        pass

    def load(self, path : str) -> np:
        img_ = img.imread(path)
        print(f"Loading image of dimension {img_.shape[0]} x {img_.shape[1]}")
        return np.array(img_)

    def display(self, array : np ) -> None:
        plt.imshow(array)
        plt.show()

