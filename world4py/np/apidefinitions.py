'''Definition of WORLD apis
'''

import ctypes
import numpy
from numpy.ctypeslib import ndpointer

from world4py.np import structures, instance


_CheapTrick = instance._WORLD.CheapTrick
_CheapTrick.restype = None
_CheapTrick.argtypes = [ndpointer(dtype=numpy.float64, ndim=1, flags='C'), ctypes.c_int, ctypes.c_int,
                       ndpointer(dtype=numpy.float64, ndim=1, flags='C'), ndpointer(dtype=numpy.float64, ndim=1, flags='C'), ctypes.c_int,
                       ctypes.POINTER(structures.CheapTrickOption), ndpointer(dtype=numpy.uintp, ndim=1, flags='C')]
                       
_InitializeCheapTrickOption = instance._WORLD.InitializeCheapTrickOption
_InitializeCheapTrickOption.restype = None
_InitializeCheapTrickOption.argtypes = [ctypes.c_int, ctypes.POINTER(structures.CheapTrickOption)]

_GetFFTSizeForCheapTrick = instance._WORLD.GetFFTSizeForCheapTrick
_GetFFTSizeForCheapTrick.restype = ctypes.c_int
_GetFFTSizeForCheapTrick.argtypes = [ctypes.c_int, ctypes.POINTER(structures.CheapTrickOption)]

_GetF0FloorForCheapTrick = instance._WORLD.GetF0FloorForCheapTrick
_GetF0FloorForCheapTrick.restype = ctypes.c_double
_GetF0FloorForCheapTrick.argtypes = [ctypes.c_int, ctypes.c_int]

_GetNumberOfAperiodicities = instance._WORLD.GetNumberOfAperiodicities
_GetNumberOfAperiodicities.restype = ctypes.c_int
_GetNumberOfAperiodicities.argtypes = [ctypes.c_int]

_CodeAperiodicity = instance._WORLD.CodeAperiodicity
_CodeAperiodicity.restype = None
_CodeAperiodicity.argtypes = [ndpointer(dtype=numpy.uintp, ndim=1, flags='C'), ctypes.c_int,
                             ctypes.c_int, ctypes.c_int, ndpointer(dtype=numpy.uintp, ndim=1, flags='C')]

_DecodeAperiodicity = instance._WORLD.DecodeAperiodicity
_DecodeAperiodicity.restype = None
_DecodeAperiodicity.argtypes = [ndpointer(dtype=numpy.uintp, ndim=1, flags='C'),
                               ctypes.c_int, ctypes.c_int, ctypes.c_int, ndpointer(dtype=numpy.uintp, ndim=1, flags='C')]

_CodeSpectralEnvelope = instance._WORLD.CodeSpectralEnvelope
_CodeSpectralEnvelope.restype = None
_CodeSpectralEnvelope.argtypes = [ndpointer(dtype=numpy.uintp, ndim=1, flags='C'), ctypes.c_int,
                                 ctypes.c_int, ctypes.c_int, ctypes.c_int,
                                 ndpointer(dtype=numpy.uintp, ndim=1, flags='C')]

_DecodeSpectralEnvelope = instance._WORLD.DecodeSpectralEnvelope
_DecodeSpectralEnvelope.restype = None
_DecodeSpectralEnvelope.argtypes = [ndpointer(dtype=numpy.uintp, ndim=1, flags='C'),
                                   ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
                                   ndpointer(dtype=numpy.uintp, ndim=1, flags='C')]

_D4C = instance._WORLD.D4C
_D4C.restype = None
_D4C.argtypes = [ndpointer(dtype=numpy.float64, ndim=1, flags='C'), ctypes.c_int, ctypes.c_int,
                ndpointer(dtype=numpy.float64, ndim=1, flags='C'), ndpointer(dtype=numpy.float64, ndim=1, flags='C'), ctypes.c_int,
                ctypes.c_int, ctypes.POINTER(structures.D4COption), ndpointer(dtype=numpy.uintp, ndim=1, flags='C')]

_InitializeD4COption = instance._WORLD.InitializeD4COption
_InitializeD4COption.restype = None
_InitializeD4COption.argtypes = [ctypes.POINTER(structures.D4COption)]

_Dio = instance._WORLD.Dio
_Dio.restype = None
_Dio.argtypes = [ndpointer(dtype=numpy.float64, ndim=1, flags='C'), ctypes.c_int, ctypes.c_int, ctypes.POINTER(structures.DioOption),
                ndpointer(dtype=numpy.float64, ndim=1, flags='C'), ndpointer(dtype=numpy.float64, ndim=1, flags='C')]

_InitializeDioOption = instance._WORLD.InitializeDioOption
_InitializeDioOption.restype = None
_InitializeDioOption.argtypes = [ctypes.POINTER(structures.DioOption)]

_GetSamplesForDIO = instance._WORLD.GetSamplesForDIO
_GetSamplesForDIO.restype = ctypes.c_int
_GetSamplesForDIO.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_double]

_Harvest = instance._WORLD.Harvest
_Harvest.restype = None
_Harvest.argtypes = [ndpointer(dtype=numpy.float64, ndim=1, flags='C'), ctypes.c_int, ctypes.c_int,
                    ctypes.POINTER(structures.HarvestOption), ndpointer(dtype=numpy.float64, ndim=1, flags='C'), ndpointer(dtype=numpy.float64, ndim=1, flags='C')]

_InitializeHarvestOption = instance._WORLD.InitializeHarvestOption
_InitializeHarvestOption.restype = None
_InitializeHarvestOption.argtypes = [ctypes.POINTER(structures.HarvestOption)]

_GetSamplesForHarvest = instance._WORLD.GetSamplesForHarvest
_GetSamplesForHarvest.restype = ctypes.c_int
_GetSamplesForHarvest.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_double]

_StoneMask = instance._WORLD.StoneMask
_StoneMask.restype = None
_StoneMask.argtypes = [ndpointer(dtype=numpy.float64, ndim=1, flags='C'), ctypes.c_int, ctypes.c_int,
                      ndpointer(dtype=numpy.float64, ndim=1, flags='C'), ndpointer(dtype=numpy.float64, ndim=1, flags='C'), ctypes.c_int,
                      ndpointer(dtype=numpy.float64, ndim=1, flags='C')]

_Synthesis = instance._WORLD.Synthesis
_Synthesis.restype = None
_Synthesis.argtypes = [ndpointer(dtype=numpy.float64, ndim=1, flags='C'), ctypes.c_int,
                      ndpointer(dtype=numpy.uintp, ndim=1, flags='C'), ndpointer(dtype=numpy.uintp, ndim=1, flags='C'),
                      ctypes.c_int, ctypes.c_double, ctypes.c_int, ctypes.c_int, ndpointer(dtype=numpy.float64, ndim=1, flags='C')]

_InitializeSynthesizer = instance._WORLD.InitializeSynthesizer
_InitializeSynthesizer.restype = None
_InitializeSynthesizer.argtypes = [ctypes.c_int, ctypes.c_double, ctypes.c_int,
                                  ctypes.c_int, ctypes.c_int, ctypes.POINTER(structures.WorldSynthesizer)]

_AddParameters = instance._WORLD.AddParameters
_AddParameters.restype = ctypes.c_int
_AddParameters.argtypes = [ndpointer(dtype=numpy.float64, ndim=1, flags='C'), ctypes.c_int, ndpointer(dtype=numpy.uintp, ndim=1, flags='C'),
                          ndpointer(dtype=numpy.uintp, ndim=1, flags='C'), ctypes.POINTER(structures.WorldSynthesizer)]

_RefreshSynthesizer = instance._WORLD.RefreshSynthesizer
_RefreshSynthesizer.restype = None
_RefreshSynthesizer.argtypes = [ctypes.POINTER(structures.WorldSynthesizer)]

_DestroySynthesizer = instance._WORLD.DestroySynthesizer
_DestroySynthesizer.restype = None
_DestroySynthesizer.argtypes = [ctypes.POINTER(structures.WorldSynthesizer)]

_IsLocked = instance._WORLD.IsLocked
_IsLocked.restype = ctypes.c_int
_IsLocked.argtypes = [ctypes.POINTER(structures.WorldSynthesizer)]

_Synthesis2 = instance._WORLD.Synthesis2
_Synthesis2.restype = ctypes.c_int
_Synthesis2.argtypes = [ctypes.POINTER(structures.WorldSynthesizer)]
