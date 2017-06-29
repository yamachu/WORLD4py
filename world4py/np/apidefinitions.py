'''Definition of WORLD apis
'''

import ctypes
import numpy
from numpy.ctypeslib import ndpointer

from world4py import helper
from world4py.np import structures, instance


_CheapTrick = helper._safe_func_modify(instance._WORLD,
    'CheapTrick', None,
    [ndpointer(dtype=numpy.float64, ndim=1, flags='C'), ctypes.c_int, ctypes.c_int,
     ndpointer(dtype=numpy.float64, ndim=1, flags='C'), ndpointer(dtype=numpy.float64, ndim=1, flags='C'), ctypes.c_int,
     ctypes.POINTER(structures.CheapTrickOption), ndpointer(dtype=numpy.uintp, ndim=1, flags='C')])
                       
_InitializeCheapTrickOption = helper._safe_func_modify(instance._WORLD,
    'InitializeCheapTrickOption', None,
    [ctypes.c_int, ctypes.POINTER(structures.CheapTrickOption)])

_GetFFTSizeForCheapTrick = helper._safe_func_modify(instance._WORLD,
    'GetFFTSizeForCheapTrick', ctypes.c_int,
    [ctypes.c_int, ctypes.POINTER(structures.CheapTrickOption)])

_GetF0FloorForCheapTrick = helper._safe_func_modify(instance._WORLD,
    'GetF0FloorForCheapTrick', ctypes.c_double, [ctypes.c_int, ctypes.c_int])

_GetNumberOfAperiodicities = helper._safe_func_modify(instance._WORLD,
    'GetNumberOfAperiodicities', ctypes.c_int, [ctypes.c_int])

_CodeAperiodicity = helper._safe_func_modify(instance._WORLD,
    'CodeAperiodicity', None,
    [ndpointer(dtype=numpy.uintp, ndim=1, flags='C'), ctypes.c_int,
     ctypes.c_int, ctypes.c_int, ndpointer(dtype=numpy.uintp, ndim=1, flags='C')])

_DecodeAperiodicity = helper._safe_func_modify(instance._WORLD,
    'DecodeAperiodicity', None,
    [ndpointer(dtype=numpy.uintp, ndim=1, flags='C'),
     ctypes.c_int, ctypes.c_int, ctypes.c_int, ndpointer(dtype=numpy.uintp, ndim=1, flags='C')])

_CodeSpectralEnvelope = helper._safe_func_modify(instance._WORLD,
    'CodeSpectralEnvelope', None,
    [ndpointer(dtype=numpy.uintp, ndim=1, flags='C'), ctypes.c_int,
     ctypes.c_int, ctypes.c_int, ctypes.c_int,
     ndpointer(dtype=numpy.uintp, ndim=1, flags='C')])

_DecodeSpectralEnvelope = helper._safe_func_modify(instance._WORLD,
    'DecodeSpectralEnvelope', None,
    [ndpointer(dtype=numpy.uintp, ndim=1, flags='C'),
     ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
     ndpointer(dtype=numpy.uintp, ndim=1, flags='C')])

_D4C = helper._safe_func_modify(instance._WORLD,
    'D4C', None,
    [ndpointer(dtype=numpy.float64, ndim=1, flags='C'), ctypes.c_int, ctypes.c_int,
     ndpointer(dtype=numpy.float64, ndim=1, flags='C'), ndpointer(dtype=numpy.float64, ndim=1, flags='C'), ctypes.c_int,
     ctypes.c_int, ctypes.POINTER(structures.D4COption), ndpointer(dtype=numpy.uintp, ndim=1, flags='C')])

_InitializeD4COption = helper._safe_func_modify(instance._WORLD,
    'InitializeD4COption', None,
    [ctypes.POINTER(structures.D4COption)])

_Dio = helper._safe_func_modify(instance._WORLD,
    'Dio', None,
    [ndpointer(dtype=numpy.float64, ndim=1, flags='C'), ctypes.c_int, ctypes.c_int, ctypes.POINTER(structures.DioOption),
     ndpointer(dtype=numpy.float64, ndim=1, flags='C'), ndpointer(dtype=numpy.float64, ndim=1, flags='C')])

_InitializeDioOption = helper._safe_func_modify(instance._WORLD,
    'InitializeDioOption', None, [ctypes.POINTER(structures.DioOption)])

_GetSamplesForDIO = helper._safe_func_modify(instance._WORLD,
    'GetSamplesForDIO', ctypes.c_int, [ctypes.c_int, ctypes.c_int, ctypes.c_double])

_Harvest = helper._safe_func_modify(instance._WORLD,
    'Harvest', None,
    [ndpointer(dtype=numpy.float64, ndim=1, flags='C'), ctypes.c_int, ctypes.c_int,
     ctypes.POINTER(structures.HarvestOption), ndpointer(dtype=numpy.float64, ndim=1, flags='C'),
     ndpointer(dtype=numpy.float64, ndim=1, flags='C')])

_InitializeHarvestOption = helper._safe_func_modify(instance._WORLD,
    'InitializeHarvestOption', None, [ctypes.POINTER(structures.HarvestOption)])

_GetSamplesForHarvest = helper._safe_func_modify(instance._WORLD,
    'GetSamplesForHarvest', ctypes.c_int,
    [ctypes.c_int, ctypes.c_int, ctypes.c_double])

_StoneMask = helper._safe_func_modify(instance._WORLD,
    'StoneMask', None,
    [ndpointer(dtype=numpy.float64, ndim=1, flags='C'), ctypes.c_int, ctypes.c_int,
     ndpointer(dtype=numpy.float64, ndim=1, flags='C'), ndpointer(dtype=numpy.float64, ndim=1, flags='C'), ctypes.c_int,
     ndpointer(dtype=numpy.float64, ndim=1, flags='C')])

_Synthesis = helper._safe_func_modify(instance._WORLD,
    'Synthesis', None,
    [ndpointer(dtype=numpy.float64, ndim=1, flags='C'), ctypes.c_int,
     ndpointer(dtype=numpy.uintp, ndim=1, flags='C'), ndpointer(dtype=numpy.uintp, ndim=1, flags='C'),
     ctypes.c_int, ctypes.c_double, ctypes.c_int, ctypes.c_int, ndpointer(dtype=numpy.float64, ndim=1, flags='C')])

_InitializeSynthesizer = helper._safe_func_modify(instance._WORLD,
    'InitializeSynthesizer', None,
    [ctypes.c_int, ctypes.c_double, ctypes.c_int,
     ctypes.c_int, ctypes.c_int, ctypes.POINTER(structures.WorldSynthesizer)])

_AddParameters = helper._safe_func_modify(instance._WORLD,
    'AddParameters', ctypes.c_int,
    [ndpointer(dtype=numpy.float64, ndim=1, flags='C'), ctypes.c_int, ndpointer(dtype=numpy.uintp, ndim=1, flags='C'),
     ndpointer(dtype=numpy.uintp, ndim=1, flags='C'), ctypes.POINTER(structures.WorldSynthesizer)])

_RefreshSynthesizer = helper._safe_func_modify(instance._WORLD,
    'RefreshSynthesizer', None, [ctypes.POINTER(structures.WorldSynthesizer)])

_DestroySynthesizer = helper._safe_func_modify(instance._WORLD,
    'DestroySynthesizer', None, [ctypes.POINTER(structures.WorldSynthesizer)])

_IsLocked = helper._safe_func_modify(instance._WORLD,
    'IsLocked', ctypes.c_int, [ctypes.POINTER(structures.WorldSynthesizer)])

_Synthesis2 = helper._safe_func_modify(instance._WORLD,
    'Synthesis2', ctypes.c_int, [ctypes.POINTER(structures.WorldSynthesizer)])
