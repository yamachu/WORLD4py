'''Definition of WORLD tools (audioio, parameterio)
'''

import ctypes

from world4py import helper
from world4py.native import instance


_wavwrite = helper._safe_func_modify(instance._WORLD,
    'wavwrite', None, 
    [ctypes.POINTER(ctypes.c_double), ctypes.c_int, ctypes.c_int, ctypes.c_int,
     ctypes.c_char_p])

_GetAudioLength = helper._safe_func_modify(instance._WORLD,
    'GetAudioLength', ctypes.c_int, [ctypes.c_char_p])

_wavread = helper._safe_func_modify(instance._WORLD,
    'wavread', ctypes.c_int,
    [ctypes.c_char_p, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int),
     ctypes.POINTER(ctypes.c_double)])

_WriteF0 = helper._safe_func_modify(instance._WORLD,
    'WriteF0', None,
    [ctypes.c_char_p, ctypes.c_int, ctypes.c_double,
     ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_int])

_ReadF0 = helper._safe_func_modify(instance._WORLD,
    'ReadF0', ctypes.c_int,
    [ctypes.c_char_p, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)])

_GetHeaderInformation = helper._safe_func_modify(instance._WORLD,
    'GetHeaderInformation', ctypes.c_double, [ctypes.c_char_p, ctypes.c_char_p])

_WriteSpectralEnvelope = helper._safe_func_modify(instance._WORLD,
    'WriteSpectralEnvelope', None,
    [ctypes.c_char_p, ctypes.c_int, ctypes.c_int,
     ctypes.c_double, ctypes.c_int, ctypes.c_int,
     ctypes.POINTER(ctypes.POINTER(ctypes.c_double))])

_ReadSpectralEnvelope = helper._safe_func_modify(instance._WORLD,
    'ReadSpectralEnvelope', ctypes.c_int,
    [ctypes.c_char_p, ctypes.POINTER(ctypes.POINTER(ctypes.c_double))])

_WriteAperiodicity = helper._safe_func_modify(instance._WORLD,
    'WriteAperiodicity', None,
    [ctypes.c_char_p, ctypes.c_int, ctypes.c_int,
     ctypes.c_double, ctypes.c_int, ctypes.c_int,
     ctypes.POINTER(ctypes.POINTER(ctypes.c_double))])

_ReadAperiodicity = helper._safe_func_modify(instance._WORLD,
    'ReadAperiodicity', ctypes.c_int,
    [ctypes.c_char_p, ctypes.POINTER(ctypes.POINTER(ctypes.c_double))])
