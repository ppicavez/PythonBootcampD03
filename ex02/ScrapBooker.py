import numpy as np


class ScrapBooker():
    def crop(self, my_array, dimensions, position=(0, 0)):
        x_begin = position[0]
        x_end = position[0] + dimensions[0]
        p_begin = position[1]
        y_end = position[1] + dimensions[1]
        if x_end > len(my_array) or y_end > len(my_array[0]):
            print("dimensions is larger than the current image size")
            return my_array
        return my_array[x_begin:x_end, y_begin:y_end]

    def thin(self, my_array, n, axis):
        if axis:
            for i in range(n-1, len(my_array), n-1):
                my_array = np.concatenate((my_array[:i, :],
                                          my_array[i+1:, :]), axis=0)
            return my_array
        else:
            for i in range(n-1, len(my_array[0]), n-1):
                my_array = np.concatenate((my_array[:, :i],
                                           my_array[:, i+1:]), axis=1)
            return my_array

    def juxtapose(self, my_array, n, axis):
        copy = my_array
        for i in range(n-1):
            my_array = np.concatenate((my_array, copy), axis=axis)
        return my_array

    def mosaic(self, my_array, dimensions):
        my_array = ScrapBooker.juxtapose(self, my_array, dimensions[0], 0)
        return ScrapBooker.juxtapose(self, my_array, dimensions[1], 1)


if __name__ == "__main__":
    my_scrap = ScrapBooker()
    my_arr = np.eye(2)
    print(my_arr)
    print("\nMosaic (2x3) :\n")
    my_arr_bis = my_scrap.mosaic(my_arr, (2, 3))
    print(my_arr_bis)
    print("\nCrop to 3x4 from index [1,1] :\n")
    my_arr_ter = my_scrap.crop(my_arr, (3, 4), (1, 1))
    print(my_arr_ter)
    print("\nThin every third line vertically (n=3, axis=0)\n")
    my_arr_quart = my_scrap.thin(my_arr, 3, 0)
    print(my_arr_quart)
