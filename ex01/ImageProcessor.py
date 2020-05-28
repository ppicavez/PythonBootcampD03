import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


class ImageProcessor():
    def load(self, path):
        img = mpimg.imread(path)
        arr = np.array(img)
        print("Image of dimensions {} x {}".format(len(arr), len(arr[0])))
        return arr

    def display(self, array):
        imgplot = plt.imshow(array)
        plt.show()
