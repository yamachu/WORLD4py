'''Utils of ctypes
'''

import ctypes


def cast_1d_pointer_to_1d_list(ctype_1d_pointer_value):
    '''Cast ctypes's 1d-pointer or 1d-array to Python 1d-List

    Args:
        ctype_1d_pointer_value (POINTER(c_types object)): 1d-pointer of c_types objects

    Returns:
        List(python object like c_types): Python cast list
    '''
    return list(ctype_1d_pointer_value)


def cast_2d_pointer_to_2d_list(ctype_2d_pointer_value, outer_rank, inner_rank):
    '''Cast ctypes's 2d-pointer or 2d-array to Python 2d-List

    Args:
        ctype_2d_pointer_value (POINTER(POINTER(c_types object))): 2d-pointer of c_types objects
        outer_rank (int): outer dimention of list
        inner_rank (int): inner dimention of list

    Returns:
        List(python object like c_types): Python cast list
    '''
    return [[ctype_2d_pointer_value[o][i] for i in range(inner_rank)]
            for o in range(outer_rank)]


def cast_1d_list_to_1d_pointer(list_value_1d, c_type=ctypes.c_double):
    '''Cast Python 1d-list to 1d-pointer of c_types

    Args:
        list_value_1d (List[:object:]): 1d-Python list
        c_type (ctypes, default: ctypes.c_double): target type

    Returns:
        POINTER(c_type): ctypes 1d-pointer
    '''
    return (c_type * len(list_value_1d))(*list_value_1d)


def cast_2d_list_to_2d_pointer(list_value_2d, c_type=ctypes.c_double):
    '''Cast Python 2d-list to 2d-pointer of c_types

    Args:
        list_value_2d (List[List[:object:]]): 2d-Python list
        c_type (ctypes, default: ctypes.c_double): target type

    Returns:
        POINTER(POINTER(c_type)): ctypes 2d-pointer
    '''
    inner_arr_type = c_type * len(list_value_2d[0])
    outer_arr_type = inner_arr_type * len(list_value_2d)
    tmp_buffer = outer_arr_type()

    pointer_2d = ctypes.cast(tmp_buffer, ctypes.POINTER(ctypes.POINTER(c_type)))
    outer_size = len(list_value_2d)

    for i in range(outer_size):
        pointer_2d[i] = ctypes.cast(inner_arr_type(*list_value_2d[i]), ctypes.POINTER(c_type))

    return pointer_2d
