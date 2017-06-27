'''Utils of numpy
'''

import numpy


def get_2d_pointer(numpy_2d_array):
    '''Get 2d uint pointer from 2d numpy array

    Args:
        numpy_2d_array (ndarray(ndim=2)): 2d-numpy array

    Returns:
        ndarray((numpy_2d_array.shape[0],), ndim=1): numpy uintp array

    Notice:
        See Original: Sturla Molden's method
            http://numpy-discussion.10968.n7.nabble.com/Pass-2d-ndarray-into-C-double-using-ctypes-tp39414p39416.html
    '''

    return (numpy_2d_array.__array_interface__['data'][0]
            + numpy.arange(numpy_2d_array.shape[0]) * numpy_2d_array.strides[0]).astype(numpy.uintp)
