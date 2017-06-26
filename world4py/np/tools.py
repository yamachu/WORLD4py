'''Tools of WORLD (audioio, parameterio)
'''

import ctypes
import numpy

from world4py.np import toolsdefinitions


def get_wave_parameters(filename):
    '''Get waveform and some infomation

    Args:
        filename (str): Filename of the input file path

    Returns:
        ndarray(dtype=double, ndim=1): Waveform (-1.0 ~ 1.0)
        int: Sampling frequency [Hz]
        int: Quantization bit [bit]
    '''
    x_len = toolsdefinitions._GetAudioLength(filename.encode('utf-8'))
    fs = ctypes.c_int()
    nbit = ctypes.c_int()

    x = numpy.zeros(x_len, dtype=numpy.float64)

    toolsdefinitions._wavread(filename.encode('utf-8'), ctypes.byref(fs), ctypes.byref(nbit), x)

    return x, fs.value, nbit.value


def write_wav_file(filename, wav, fs, nbit):
    '''Write waveform to file

    Args:
        filename (str): Name of the output file path
        wav (ndarray(dtype=double, ndim=1)): Waveform (-1.0 ~ 1.0)
        fs (int): Sampling frequency [Hz]
        nbit (int): Quantization bit [bit]

    Notice:
        This function only supports the 16bit
    '''

    toolsdefinitions._wavwrite(wav, len(wav), fs, nbit, filename.encode('utf-8'))
