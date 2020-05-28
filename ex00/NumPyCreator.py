import numpy as np


class NumPyCreator():

    def from_list(self, lst):
        return np.array(lst)

    def from_tuple(self, tpl):
        return np.array(tpl)

    def from_iterable(self, itr):
        return np.array(itr)

    def from_shape(self, shape, value):
        return np.full(shape, value)

    def random(self, shape):
        return np.random.random(shape)

    def identity(self, n):
        return np.identity(n)


if __name__ == "__main__":
    my_numpy = NumPyCreator()
    np1 = my_numpy.from_list([0, 1, 2, 3])
    print(np1)
    np2 = my_numpy.from_tuple((0, 1, 2, 3, 4))
    print(np2)
    np3 = my_numpy.from_iterable(range(0, 10))
    print(np3)
    np4 = my_numpy.random((3, 10))
    print(np4)
    np5 = my_numpy.from_shape((10, 3), 5)
    print(np5)
    np5 = my_numpy.identity(3)
    print(np5)
