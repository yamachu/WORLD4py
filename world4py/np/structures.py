'''Definition of Option Structures of WORLD
'''

import ctypes


class CheapTrickOption(ctypes.Structure):
    '''heapTrickOption

    Attributes:
        q1: c_double        Parameter of decode spectrum
        f0_floor: c_double  For deciding fft_size
        fft_size: c_int     fft_size
    '''

    _fields_ = [
        ("q1", ctypes.c_double),
        ("f0_floor", ctypes.c_double),
        ("fft_size", ctypes.c_int),
    ]


class D4COption(ctypes.Structure):
    '''D4COption

    Attributes:
        threshold: c_double To determine frame is unvoice or not
                            (high value is tending to regard as unvoiced)
    '''

    _fields_ = [
        ("threshold", ctypes.c_double),
    ]


class DioOption(ctypes.Structure):
    '''DioOption

    Attributes:
        f0_floor: c_doube               Floor of F0 estimation
        f0_ceil: c_double               Ceil of F0 estimation
        channels_in_octave: c_double    see ref WORLD
        frame_period: c_double          Frame shift [ms]
        speed: c_int                    For downsampling (fs / speed)
        allowed_range: c_double         To determine F0 is unvoiced or not
                                        when value is 0, most strictly and counted as unvoiced
    '''

    _fields_ = [
        ("f0_floor", ctypes.c_double),
        ("f0_ceil", ctypes.c_double),
        ("channels_in_octave", ctypes.c_double),
        ("frame_period", ctypes.c_double),
        ("speed", ctypes.c_int),
        ("allowed_range", ctypes.c_double),
    ]


class HarvestOption(ctypes.Structure):
    '''HarvestOption

    Attributes:
        f0_floor: c_doube               Floor of F0 estimation
        f0_ceil: c_double               Ceil of F0 estimation
        frame_period: c_double          Length of per-frame [ms]
    '''

    _fields_ = [
        ('f0_floor', ctypes.c_double),
        ('f0_ceil', ctypes.c_double),
        ('frame_period', ctypes.c_double),
    ]


class WorldSynthesizer(ctypes.Structure):
    '''WorldSynthesizer - Container of Realtime synthesis state

    Should not access members except for buffer
    Synthesis parameter should be set via InitializeSynthesizer and AddPamameters

    Attributes:
        buffer: POINTER(c_double)
    '''


    _fields_ = [
        ('fs', ctypes.c_int),
        ('frame_period', ctypes.c_double),
        ('buffer_size', ctypes.c_int),
        ('number_of_pointers', ctypes.c_int),
        ('fft_size', ctypes.c_int),

        ('buffer', ctypes.POINTER(ctypes.c_double)), # length is same of buffer_size
        ('current_pointer', ctypes.c_int),
        ('i', ctypes.c_int),

        ('dc_remover', ctypes.POINTER(ctypes.c_double)),

        ('f0_length', ctypes.POINTER(ctypes.c_int)),
        ('f0_origin', ctypes.POINTER(ctypes.c_int)),
        ('spectrogram', ctypes.POINTER(ctypes.POINTER(ctypes.POINTER(ctypes.c_double)))),
        ('aperiodicity', ctypes.POINTER(ctypes.POINTER(ctypes.POINTER(ctypes.c_double)))),

        ('current_pointer2', ctypes.c_int),
        ('head_pointer', ctypes.c_int),
        ('synthesized_sample', ctypes.c_int),

        ('handoff', ctypes.c_int),
        ('handoff_phase', ctypes.c_double),
        ('handoff_f0', ctypes.c_double),
        ('last_location', ctypes.c_int),

        ('cumulative_frame', ctypes.c_int),
        ('current_frame', ctypes.c_int),

        ('interpolated_vuv', ctypes.POINTER(ctypes.POINTER(ctypes.c_double))),
        ('pulse_locations', ctypes.POINTER(ctypes.POINTER(ctypes.c_double))),
        ('pulse_locations_index', ctypes.POINTER(ctypes.POINTER(ctypes.c_int))),
        ('number_of_pulses', ctypes.POINTER(ctypes.c_int)),

        ('impulse_response', ctypes.POINTER(ctypes.c_double)),

        ('minimum_phase', ctypes.c_void_p),
        ('inverse_real_fft', ctypes.c_void_p),
        ('forward_real_fft', ctypes.c_void_p),
    ]
