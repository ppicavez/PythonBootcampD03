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


class ColorFilter():
    def invert(self, array):
        return 1 - array

    def to_blue(self, array):
        new = np.zeros(array.shape)
        new[:, :, 0] = np.zeros(array[:, :, 0].shape)
        new[:, :, 1] = np.zeros(array[:, :, 1].shape)
        new[:, :, 2] = array[:, :, 2]
        return new

    def to_green(self, array):
        return array * [0, 1, 0]

    def to_red(self, array):
        return array - self.to_blue(array) - self.to_green(array)

    def to_celluloid(self, array, tresh=4):
        new = np.array(array)
        thresolds = np.linspace(0.0, 1.0, num=tresh, endpoint=False)[::-1]
        for thresold in thresolds:
            pixels_indexes = array >= thresold
            array[pixels_indexes] = -100
            new[pixels_indexes] = thresold
        return new
