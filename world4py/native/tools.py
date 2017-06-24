'''Tools of WORLD (audioio, parameterio)
'''

import ctypes

from world4py.native import toolsdefinitions


def get_wave_parameters(filename):
    '''Get waveform and some infomation

    Args:
        filename (str): Filename of the input file path

    Returns:
        POINTER(c_double): Waveform (-1.0 ~ 1.0)
        int: Sampling frequency [Hz]
        int: Quantization bit [bit]
    '''
    x_len = toolsdefinitions._GetAudioLength(filename.encode('utf-8'))
    fs = ctypes.c_int()
    nbit = ctypes.c_int()

    x = (ctypes.c_double * x_len)()

    toolsdefinitions._wavread(filename.encode('utf-8'), ctypes.byref(fs), ctypes.byref(nbit), x)

    return x, fs.value, nbit.value


def write_wav_file(filename, wav, fs, nbit):
    '''Write waveform to file

    Args:
        filename (str): Name of the output file path
        wav (POINTER(c_double)): Waveform (-1 ~ 1)
        fs (int): Sampling frequency [Hz]
        nbit (int): Quantization bit [bit]

    Notice:
        This function only supports the 16bit
    '''

    toolsdefinitions._wavwrite(wav, len(list(wav)), fs, nbit, filename.encode('utf-8'))
