'''Definition of WORLD apis
'''

import ctypes

from world4py import helper
from world4py.native import structures, instance


_CheapTrick = helper._safe_func_modify(instance._WORLD,
    'CheapTrick', None,
    [ctypes.POINTER(ctypes.c_double), ctypes.c_int, ctypes.c_int,
     ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_int,
     ctypes.POINTER(structures.CheapTrickOption), ctypes.POINTER(ctypes.POINTER(ctypes.c_double))])

_InitializeCheapTrickOption = helper._safe_func_modify(instance._WORLD,
    'InitializeCheapTrickOption', None,
    [ctypes.c_int, ctypes.POINTER(structures.CheapTrickOption)])

_GetFFTSizeForCheapTrick = helper._safe_func_modify(instance._WORLD,
    'GetFFTSizeForCheapTrick', ctypes.c_int,
    [ctypes.c_int, ctypes.POINTER(structures.CheapTrickOption)])

_GetF0FloorForCheapTrick = helper._safe_func_modify(instance._WORLD,
    'GetF0FloorForCheapTrick', ctypes.c_double,
    [ctypes.c_int, ctypes.c_int])

_GetNumberOfAperiodicities = helper._safe_func_modify(instance._WORLD,
    'GetNumberOfAperiodicities', ctypes.c_int,
    [ctypes.c_int])

_CodeAperiodicity = helper._safe_func_modify(instance._WORLD,
    'CodeAperiodicity', None,
    [ctypes.POINTER(ctypes.POINTER(ctypes.c_double)), ctypes.c_int,
     ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.POINTER(ctypes.c_double))])

_DecodeAperiodicity = helper._safe_func_modify(instance._WORLD,
    'DecodeAperiodicity', None,
    [ctypes.POINTER(ctypes.POINTER(ctypes.c_double)),
     ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.POINTER(ctypes.c_double))])

_CodeSpectralEnvelope = helper._safe_func_modify(instance._WORLD,
    'CodeSpectralEnvelope', None,
    [ctypes.POINTER(ctypes.POINTER(ctypes.c_double)), ctypes.c_int,
     ctypes.c_int, ctypes.c_int, ctypes.c_int,
     ctypes.POINTER(ctypes.POINTER(ctypes.c_double))])

_DecodeSpectralEnvelope = helper._safe_func_modify(instance._WORLD,
    'DecodeSpectralEnvelope', None,
    [ctypes.POINTER(ctypes.POINTER(ctypes.c_double)),
     ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
     ctypes.POINTER(ctypes.POINTER(ctypes.c_double))])

_D4C = helper._safe_func_modify(instance._WORLD,
    'D4C', None,
    [ctypes.POINTER(ctypes.c_double), ctypes.c_int, ctypes.c_int,
     ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_int,
     ctypes.c_int, ctypes.POINTER(structures.D4COption), ctypes.POINTER(ctypes.POINTER(ctypes.c_double))])

_InitializeD4COption = helper._safe_func_modify(instance._WORLD,
    'InitializeD4COption', None,
    [ctypes.POINTER(structures.D4COption)])

_Dio = helper._safe_func_modify(instance._WORLD,
    'Dio', None,
    [ctypes.POINTER(ctypes.c_double), ctypes.c_int, ctypes.c_int, ctypes.POINTER(structures.DioOption),
     ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)])

_InitializeDioOption = helper._safe_func_modify(instance._WORLD,
    'InitializeDioOption', None,
    [ctypes.POINTER(structures.DioOption)])

_GetSamplesForDIO = helper._safe_func_modify(instance._WORLD,
    'GetSamplesForDIO', ctypes.c_int,
    [ctypes.c_int, ctypes.c_int, ctypes.c_double])

_Harvest = helper._safe_func_modify(instance._WORLD,
    'Harvest', None,
    [ctypes.POINTER(ctypes.c_double), ctypes.c_int, ctypes.c_int,
     ctypes.POINTER(structures.HarvestOption), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)])

_InitializeHarvestOption = helper._safe_func_modify(instance._WORLD,
    'InitializeHarvestOption', None,
    [ctypes.POINTER(structures.HarvestOption)])

_GetSamplesForHarvest = helper._safe_func_modify(instance._WORLD,
    'GetSamplesForHarvest', ctypes.c_int,
    [ctypes.c_int, ctypes.c_int, ctypes.c_double])

_StoneMask = helper._safe_func_modify(instance._WORLD,
    'StoneMask', None,
    [ctypes.POINTER(ctypes.c_double), ctypes.c_int, ctypes.c_int,
     ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_int,
     ctypes.POINTER(ctypes.c_double)])

_Synthesis = helper._safe_func_modify(instance._WORLD,
    'Synthesis', None,
    [ctypes.POINTER(ctypes.c_double), ctypes.c_int,
     ctypes.POINTER(ctypes.POINTER(ctypes.c_double)), ctypes.POINTER(ctypes.POINTER(ctypes.c_double)),
     ctypes.c_int, ctypes.c_double, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_double)])

_InitializeSynthesizer = helper._safe_func_modify(instance._WORLD,
    'InitializeSynthesizer', None,
    [ctypes.c_int, ctypes.c_double, ctypes.c_int,
     ctypes.c_int, ctypes.c_int, ctypes.POINTER(structures.WorldSynthesizer)])

_AddParameters = helper._safe_func_modify(instance._WORLD,
    'AddParameters', ctypes.c_int,
    [ctypes.POINTER(ctypes.c_double), ctypes.c_int, ctypes.POINTER(ctypes.POINTER(ctypes.c_double)),
     ctypes.POINTER(ctypes.POINTER(ctypes.c_double)), ctypes.POINTER(structures.WorldSynthesizer)])

_RefreshSynthesizer = helper._safe_func_modify(instance._WORLD,
    'RefreshSynthesizer', None,
    [ctypes.POINTER(structures.WorldSynthesizer)])

_DestroySynthesizer = helper._safe_func_modify(instance._WORLD,
    'DestroySynthesizer', None,
    [ctypes.POINTER(structures.WorldSynthesizer)])

_IsLocked = helper._safe_func_modify(instance._WORLD,
    'IsLocked', ctypes.c_int,
    [ctypes.POINTER(structures.WorldSynthesizer)])

_Synthesis2 = helper._safe_func_modify(instance._WORLD,
    'Synthesis2', ctypes.c_int,
    [ctypes.POINTER(structures.WorldSynthesizer)])
