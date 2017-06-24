'''Container of WORLD Library Instance
'''

import ctypes

from world4py import _WORLD_LIBRARY_PATH


_WORLD = ctypes.cdll.LoadLibrary(_WORLD_LIBRARY_PATH)
