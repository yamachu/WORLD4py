'''Container of WORLD Library Instance
'''

import os
import numpy.ctypeslib

from world4py import _WORLD_LIBRARY_PATH


_WORLD = numpy.ctypeslib.load_library(
    _WORLD_LIBRARY_PATH.split(os.path.sep)[-1].split('.')[0],
    os.path.sep.join(_WORLD_LIBRARY_PATH.split(os.path.sep)[:-1]))
