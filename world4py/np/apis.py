'''APIs of WORLD
'''

import numpy

from world4py.np import apidefinitions, structures, utils


DEFAULT_F0_FLOOR = 71.0
DEFAULT_F0_CEIL = 800.0
DEFAULT_FRAME_PERIOD = 5.0


def dio(x, fs, f0_floor=DEFAULT_F0_FLOOR, f0_ceil=DEFAULT_F0_CEIL,
        channels_in_octave=2.0, frame_period=DEFAULT_FRAME_PERIOD,
        speed=1, allowed_range=0.1, **dummy):
    '''F0 extract by Dio

    Args:
        x (ndarray(dtype=double, ndim=1)): Input waveform
        fs (int): Sampling frequency [Hz]
        f0_floor (double, optional): Floor of F0 estimation
        f0_ceil (double, optional): Ceil of F0 estimation
        channels_in_octave (double, optional): should not change, default=2.0
        frame_period (double, optional): Frame shift [ms]
        speed (int, optional): For downsampling (fs / speed) (1, 2, ..., 12), default=1
        allowed_range (double, optional): To determine F0 is unvoiced or not
                                          reasonable range is 0.02 to 0.2, default=0.1

    Returns:
        ndarray(dtype=double, ndim=1): extracted F0
        ndarray(dtype=double, ndim=1): Temporal positions
    '''

    option = structures.DioOption()
    apidefinitions._InitializeDioOption(option)

    option.f0_floor = f0_floor
    option.f0_ceil = f0_ceil
    option.channels_in_octave = channels_in_octave
    option.frame_period = frame_period
    option.speed = speed
    option.allowed_range = allowed_range

    x_length = len(x)
    f0_length = apidefinitions._GetSamplesForDIO(fs, x_length, option.frame_period)

    f0 = numpy.zeros(f0_length, dtype=numpy.float64)
    time_axis = numpy.zeros(f0_length, dtype=numpy.float64)

    apidefinitions._Dio(x, x_length, fs, option, time_axis, f0)

    return f0, time_axis


def stone_mask(x, f0, fs, temporal_positions, **dummy):
    '''Refine F0 by StoneMask

    Args:
        x (ndarray(dtype=double, ndim=1)): Input waveform
        f0 (ndarray(dtype=double, ndim=1)): Extracted F0
        fs (int): Sampling frequency [Hz]
        temporal_positions (ndarray(dtype=double, ndim=1)): temporal positions

    Returns:
        ndarray(dtype=double, ndim=1): Refined F0
    '''

    f0_length = len(f0)
    refined_f0 = numpy.zeros(f0_length, dtype=numpy.float64)

    apidefinitions._StoneMask(x, len(x), fs, temporal_positions,
                              f0, f0_length, refined_f0)

    return refined_f0


def harvest(x, fs, f0_floor=DEFAULT_F0_FLOOR, f0_ceil=DEFAULT_F0_CEIL,
            frame_period=DEFAULT_FRAME_PERIOD, **dummy):
    '''F0 extract by Harvest

    Args:
        x (ndarray(dtype=double, ndim=1)): Input waveform
        fs (int): Sampling frequency [Hz]
        f0_floor (double, optional): Floor of F0 estimation
        f0_ceil (double, optional): Ceil of F0 estimation
        frame_period (double, optional): Frame shift [ms]

    Returns:
        ndarray(dtype=double, ndim=1): extracted F0
        ndarray(dtype=double, ndim=1): Temporal positions

    Notice:
        Harvest tend to consider F0 as voiced compared to Dio
    '''

    option = structures.HarvestOption()
    apidefinitions._InitializeHarvestOption(option)

    option.f0_floor = f0_floor
    option.f0_ceil = f0_ceil
    option.frame_period = frame_period

    x_length = len(x)
    f0_length = apidefinitions._GetSamplesForHarvest(fs, x_length, option.frame_period)

    f0 = numpy.zeros(f0_length, dtype=numpy.float64)
    time_axis = numpy.zeros(f0_length, dtype=numpy.float64)

    apidefinitions._Harvest(x, x_length, fs, option, time_axis, f0)

    return f0, time_axis


def cheap_trick(x, fs, temporal_positions, f0,
                q1=-0.15, f0_floor=DEFAULT_F0_FLOOR, fft_size=None, **dummy):
    '''Spectral envelope estimation by CheapTrick

    Args:
        x (ndarray(dtype=double, ndim=1)): Input waveform
        fs (int): Sampling frequency [Hz] (To determine fft_size)
        temporal_positions (ndarray(dtype=double, ndim=1)): Temporal positions
        f0 (ndarray(dtype=double, ndim=1)): Extracted F0
        q1 (double, optional): Spectral recovery parameter (should not change)
        f0_floor (double, optional): To determine fft_size
        fft_size (int, optional): When fft_size is not set, determined by fs and default f0_floor

    Returns:
        ndarray(dtype=double, ndim=2): Spectral envelope
    '''

    option = structures.CheapTrickOption()
    apidefinitions._InitializeCheapTrickOption(fs, option)

    option.q1 = q1
    if fft_size is None:
        option.f0_floor = f0_floor
        option.fft_size = apidefinitions._GetFFTSizeForCheapTrick(fs, option)
    else:
        option.fft_size = fft_size

    f0_length = len(f0)

    spectrogram = numpy.zeros((f0_length, option.fft_size // 2 + 1), dtype=numpy.float64)
    like_2d_array = utils.get_2d_pointer(spectrogram)

    apidefinitions._CheapTrick(x, len(x), fs, temporal_positions,
                               f0, f0_length, option,
                               like_2d_array)

    return spectrogram


def d4c(x, fs, temporal_positions, f0,
        threshold=0.85, f0_floor=DEFAULT_F0_FLOOR, fft_size=None, **dummy):
    '''Aperiodicity estimation by D4C

    Args:
        x (ndarray(dtype=double, ndim=1)): Input waveform
        fs (int): a
        temporal_positions (ndarray(dtype=double, ndim=1)): Temporal positions
        f0 (ndarray(dtype=double, ndim=1)): Extracted F0
        threshold (double, optional): To determine frame is unvoice or not
                            (high value is tending to regard as unvoiced)
        f0_floor (double, optional): To determine fft_size
        fft_size (double, optional): When fft_size is not set, determined by fs and default f0_floor

    Returns:
        ndarray(dtype=double, ndim=2): Aperiodicity
    '''

    option = structures.D4COption()

    apidefinitions._InitializeD4COption(option)

    option.threshold = threshold
    if fft_size is None:
        tmp_fft_size = get_fft_size(fs, f0_floor)
    else:
        tmp_fft_size = fft_size

    f0_length = len(f0)

    aperiodicity = numpy.zeros((f0_length, tmp_fft_size // 2 + 1), dtype=numpy.float64)
    like_2d_array = utils.get_2d_pointer(aperiodicity)

    apidefinitions._D4C(x, len(x), fs, temporal_positions,
                        f0, f0_length, tmp_fft_size, option,
                        like_2d_array)

    return aperiodicity


def synthesis(f0, spectrogram, aperiodicity, fs, frame_period=DEFAULT_FRAME_PERIOD):
    '''WORLD synthesis

    Args:
        f0 (ndarray(dtype=double, ndim=1)): F0
        spectrogram (ndarray(dtype=double, ndim=2)): Spectral envelope
        aperiodicity (ndarray(dtype=double, ndim=2)): Aperiodicity
        fs (int): Sampling frequency [Hz]
        frame_period (double, optional): Frame shift [ms]

    Returns:
        ndarray(dtype=double, ndim=1): Output waveform
    '''

    f0_length = len(f0)
    y_length = int(f0_length * 5.0 * fs // 1000) + 1
    y = numpy.zeros(y_length, dtype=numpy.dtype('float64'))

    fft_size = (spectrogram.shape[1] - 1) * 2

    like_2d_array_sp = utils.get_2d_pointer(spectrogram)
    like_2d_array_ap = utils.get_2d_pointer(aperiodicity)

    apidefinitions._Synthesis(f0, f0_length,
                              like_2d_array_sp, like_2d_array_ap,
                              fft_size, frame_period, fs,
                              y_length, y)

    return y


def get_fft_size(fs, f0_floor=DEFAULT_F0_FLOOR):
    '''Calculate FFT size for CheapTrick and D4C

    Args:
        fs (int): Sampling frequency [Hz]
        f0_floor (double, optional): Floor of F0

    Returns:
        int: FFT size
    '''

    option = structures.CheapTrickOption()
    option.f0_floor = f0_floor

    return apidefinitions._GetFFTSizeForCheapTrick(fs, option)


def extract_all_from_waveform(x, fs, parameters={}):
    '''Extract F0, Spectral envelope and Aperiodicity from waveform

    Args:
        x (ndarray(dtype=double, ndim=1)): Input waveform
        fs (int): Sampling frequency [Hz]
        parameters (Dict, optional): Extract parameter container
            Can configure below parameters
            {
                'Dio': bool, # use Dio or not (default use Harvest)
                'StoneMast': bool, # use StoneMask to refine F0
                'f0_floor': double,
                'f0_ceil': double,
                'channels_in_octave': double,
                'frame_period': double,
                'speed': int,
                'allowed_range': double,
                'q1': double,
                'fft_size': int,
                'threshold': double
            }

    Returns:
        (ndarray(dtype=double, ndim=1)): F0
        (ndarray(dtype=double, ndim=2)): Spectral envelope
        (ndarray(dtype=double, ndim=2)): Aperiodicity
    '''

    if parameters.get('Dio') is True:
        base_f0, time_axis = dio(x, fs, **parameters)
    else:
        base_f0, time_axis = harvest(x, fs, **parameters)
    if parameters.get('StoneMask') is True:
        f0 = stone_mask(x, base_f0, fs, time_axis)
    else:
        f0 = base_f0

    sp = cheap_trick(x, fs, time_axis, f0, **parameters)
    ap = d4c(x, fs, time_axis, f0, **parameters)

    return f0, sp, ap


def code_spectral_envelope(spectrogram, fs, number_of_dimensions):
    '''Compress spectral envelope's dimension

    Args:
        spectrogram (ndarray(dtype=double, ndim=2)): Spectral envelope
        fs (int): Sampling frequency [Hz]
        number_of_dimensions (int): Number of compressed spectral envelope's dimension

    Returns:
        ndarray(dtype=double, ndim=2): compressed spectral envelope
    '''

    f0_length = spectrogram.shape[0]
    fft_size = (spectrogram.shape[1] - 1) * 2

    coded_spectrogram = numpy.zeros((f0_length, number_of_dimensions), dtype=numpy.float64)
    like_2d_array_coded = utils.get_2d_pointer(coded_spectrogram)
    like_2d_array = utils.get_2d_pointer(spectrogram)

    apidefinitions._CodeSpectralEnvelope(like_2d_array, f0_length, fs, fft_size,
                                         number_of_dimensions, like_2d_array_coded)

    return code_spectral_envelope


def decode_spectral_envelope(coded_spectral_envelope, fs, fft_size):
    '''Restore compressed spectral envelope's dimension

    Args:
        coded_spectral_envelope (ndarray(dtype=double, ndim=2)): Coded spectral envelope
        fs (int): Sampling frequency [Hz]
        fft_size (int): FFT size

    Returns:
        ndarray(dtype=double, ndim=2): Spectral envelope
    '''

    f0_length = coded_spectral_envelope.shape[0]
    number_of_dimensions = coded_spectral_envelope.shape[1]

    spectrogram = numpy.zeros((f0_length, fft_size // 2 + 1), dtype=numpy.float64)
    like_2d_array = utils.get_2d_pointer(spectrogram)
    like_2d_array_coded = utils.get_2d_pointer(code_spectral_envelope)
    
    apidefinitions._DecodeSpectralEnvelope(like_2d_array_coded, f0_length, fs,
                                           fft_size, number_of_dimensions, like_2d_array)

    return spectrogram


def get_codec_aperiodicity_num(fs):
    '''Calculate dimension needed to code aperiodicity

    Args:
        fs (int): Sampling frequency [Hz]

    Returns:
        int: Required dimension
    '''

    return apidefinitions._GetNumberOfAperiodicities(fs)


def code_aperiodicity(aperiodicity, fs):
    '''Compress aperiodicity's dimension

    Args:
        aperiodicity (ndarray(dtype=double, ndim=2)): Aperiodicity
        fs (int): Sampling frequency [Hz]

    Returns:
        ndarray(dtype=double, ndim=2): compressed aperiodicity
    '''

    f0_length = aperiodicity.shape[0]
    fft_size = (aperiodicity.shape[1] - 1) * 2

    coded_aperiodicity = numpy.zeros((f0_length, get_codec_aperiodicity_num(fs)), dtype=numpy.float64)
    like_2d_array_coded = utils.get_2d_pointer(code_aperiodicity)
    like_2d_array = utils.get_2d_pointer(aperiodicity)
    
    apidefinitions._CodeAperiodicity(like_2d_array, f0_length, fs, fft_size,
                                     like_2d_array_coded)

    return code_aperiodicity


def decode_aperiodicity(coded_aperiodicity, fs, fft_size):
    '''Restore compressed aperiodicity's dimension

    Args:
        coded_aperiodicity (ndarray(dtype=double, ndim=2)): Coded aperiodicity
        fs (int): Sampling frequency [Hz]
        fft_size (int): FFT size

    Returns:
        ndarray(dtype=double, ndim=2): Aperiodicity
    '''

    f0_length = coded_aperiodicity.shape[0]

    aperiodicity = numpy.zeros((f0_length, fft_size // 2 + 1), dtype=numpy.float64)
    like_2d_array = utils.get_2d_pointer(aperiodicity)
    like_2d_array_coded = utils.get_2d_pointer(code_aperiodicity)

    apidefinitions._DecodeAperiodicity(coded_aperiodicity, f0_length, fs,
                                       fft_size, aperiodicity)

    return aperiodicity
