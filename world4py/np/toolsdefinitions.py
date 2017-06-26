'''Definition of WORLD tools (audioio, parameterio)
'''

import ctypes
import numpy
from numpy.ctypeslib import ndpointer

from world4py.np import instance


_wavwrite = instance._WORLD.wavwrite
_wavwrite.restype = None
_wavwrite.argtypes = [ndpointer(dtype=numpy.float64, ndim=1, flags='C'),
                      ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_char_p]

_GetAudioLength = instance._WORLD.GetAudioLength
_GetAudioLength.restype = ctypes.c_int
_GetAudioLength.argtypes = [ctypes.c_char_p]

_wavread = instance._WORLD.wavread
_wavread.restype = ctypes.c_int
_wavread.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int),
                     ndpointer(dtype=numpy.float64, ndim=1, flags='C')]

_WriteF0 = instance._WORLD.WriteF0
_WriteF0.restype = None
_WriteF0.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_double,
                     ndpointer(dtype=numpy.float64, ndim=1, flags='C'),
                     ndpointer(dtype=numpy.float64, ndim=1, flags='C'),
                     ctypes.c_int]

_ReadF0 = instance._WORLD.ReadF0
_ReadF0.restype = ctypes.c_int
_ReadF0.argtypes = [ctypes.c_char_p, ndpointer(dtype=numpy.float64, ndim=1, flags='C'),
                    ndpointer(dtype=numpy.float64, ndim=1, flags='C')]

_GetHeaderInformation = instance._WORLD.GetHeaderInformation
_GetHeaderInformation.restype = ctypes.c_double
_GetHeaderInformation.argtypes = [ctypes.c_char_p, ctypes.c_char_p]

_WriteSpectralEnvelope = instance._WORLD.WriteSpectralEnvelope
_WriteSpectralEnvelope.restype = None
_WriteSpectralEnvelope.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_int,
                                  ctypes.c_double, ctypes.c_int, ctypes.c_int,
                                  ndpointer(dtype=numpy.uintp, ndim=1, flags='C')]

_ReadSpectralEnvelope = instance._WORLD.ReadSpectralEnvelope
_ReadSpectralEnvelope.restype = ctypes.c_int
_ReadSpectralEnvelope.argtypes = [ctypes.c_char_p, ndpointer(dtype=numpy.uintp, ndim=1, flags='C')]

_WriteAperiodicity = instance._WORLD.WriteAperiodicity
_WriteAperiodicity.restype = None
_WriteAperiodicity.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_int,
                              ctypes.c_double, ctypes.c_int, ctypes.c_int,
                              ndpointer(dtype=numpy.uintp, ndim=1, flags='C')]

_ReadAperiodicity = instance._WORLD.ReadAperiodicity
_ReadAperiodicity.restype = ctypes.c_int
_ReadAperiodicity.argtypes = [ctypes.c_char_p, ndpointer(dtype=numpy.uintp, ndim=1, flags='C')]