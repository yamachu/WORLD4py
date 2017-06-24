'''APIs of WORLD
'''

import ctypes

from world4py.native import apidefinitions, structures, utils


DEFAULT_F0_FLOOR = 71.0
DEFAULT_F0_CEIL = 800.0
DEFAULT_FRAME_PERIOD = 5.0


def dio(x, fs, f0_floor=DEFAULT_F0_FLOOR, f0_ceil=DEFAULT_F0_CEIL,
        channels_in_octave=2.0, frame_period=DEFAULT_FRAME_PERIOD,
        speed=1, allowed_range=0.1, **dummy):
    '''F0 extract by Dio

    Args:
        x (POINTER(c_double)): Input waveform
        fs (int): Sampling frequency [Hz]
        f0_floor (double, optional): Floor of F0 estimation
        f0_ceil (double, optional): Ceil of F0 estimation
        channels_in_octave (double, optional): should not change, default=2.0
        frame_period (double, optional): Frame shift [ms]
        speed (int, optional): For downsampling (fs / speed) (1, 2, ..., 12), default=1
        allowed_range (double, optional): To determine F0 is unvoiced or not
                                          reasonable range is 0.02 to 0.2, default=0.1

    Returns:
        POINTER(c_double): extracted F0
        POINTER(c_double): Temporal positions
        int: F0 length
    '''

    option = structures.DioOption()
    apidefinitions._InitializeDioOption(option)

    option.f0_floor = f0_floor
    option.f0_ceil = f0_ceil
    option.channels_in_octave = channels_in_octave
    option.frame_period = frame_period
    option.speed = speed
    option.allowed_range = allowed_range

    x_length = len(list(x))
    f0_length = apidefinitions._GetSamplesForDIO(fs, x_length, option.frame_period)

    f0 = (ctypes.c_double * f0_length)()
    time_axis = (ctypes.c_double * f0_length)()

    apidefinitions._Dio(x, x_length, fs, option, time_axis, f0)

    return f0, time_axis, f0_length


def stone_mask(x, f0, fs, temporal_positions, **dummy):
    '''Refine F0 by StoneMask

    Args:
        x (POINTER(c_double)): Input waveform
        f0 (POINTER(c_double)): Extracted F0
        fs (int): Sampling frequency [Hz]
        temporal_positions (POINTER(c_double)): temporal positions

    Returns:
        POINTER(c_double): Refined F0
    '''

    f0_length = get_f0_length(f0)
    refined_f0 = (ctypes.c_double * f0_length)()

    apidefinitions._StoneMask(x, len(list(x)), fs, temporal_positions,
                              f0, f0_length, refined_f0)

    return refined_f0


def harvest(x, fs, f0_floor=DEFAULT_F0_FLOOR, f0_ceil=DEFAULT_F0_CEIL,
            frame_period=DEFAULT_FRAME_PERIOD, **dummy):
    '''F0 extract by Harvest

    Args:
        x (POINTER(c_double)): Input waveform
        fs (int): Sampling frequency [Hz]
        f0_floor (double, optional): Floor of F0 estimation
        f0_ceil (double, optional): Ceil of F0 estimation
        frame_period (double, optional): Frame shift [ms]

    Returns:
        POINTER(c_double): extracted F0
        POINTER(c_double): Temporal positions
        int: F0 length

    Notice:
        Harvest tend to consider F0 as voiced compared to Dio
    '''

    option = structures.HarvestOption()
    apidefinitions._InitializeHarvestOption(option)

    option.f0_floor = f0_floor
    option.f0_ceil = f0_ceil
    option.frame_period = frame_period

    x_length = len(list(x))
    f0_length = apidefinitions._GetSamplesForHarvest(fs, x_length, option.frame_period)

    f0 = (ctypes.c_double * f0_length)()
    time_axis = (ctypes.c_double * f0_length)()

    apidefinitions._Harvest(x, x_length, fs, option, time_axis, f0)

    return f0, time_axis, f0_length


def cheap_trick(x, fs, temporal_positions, f0,
                q1=-0.15, f0_floor=DEFAULT_F0_FLOOR, fft_size=None, **dummy):
    '''Spectral envelope estimation by CheapTrick

    Args:
        x (POINTER(c_double)): Input waveform
        fs (int): Sampling frequency [Hz] (To determine fft_size)
        temporal_positions (POINTER(c_double)): Temporal positions
        f0 (POINTER(c_double)): Extracted F0
        q1 (double, optional): Spectral recovery parameter (should not change)
        f0_floor (double, optional): To determine fft_size
        fft_size (int, optional): When fft_size is not set, determined by fs and default f0_floor

    Returns:
        POINTER(POINTER(c_double)): Spectral envelope
        int: FFT size used by CheapTrick
        Tuple(int, int): Spectrogram's shape "(f0_length, fft_size // 2 + 1)"
    '''

    option = structures.CheapTrickOption()
    apidefinitions._InitializeCheapTrickOption(fs, option)

    option.q1 = q1
    if fft_size is None:
        option.f0_floor = f0_floor
        option.fft_size = apidefinitions._GetFFTSizeForCheapTrick(fs, option)
    else:
        option.fft_size = fft_size

    f0_length = get_f0_length(f0)

    tmp_2d_array = [[0 for i in range(option.fft_size // 2 + 1)] for o in range(f0_length)]
    spectrogram = utils.cast_2d_list_to_2d_pointer(tmp_2d_array, ctypes.c_double)

    apidefinitions._CheapTrick(x, len(list(x)), fs, temporal_positions,
                               f0, f0_length, option,
                               spectrogram)

    return spectrogram, option.fft_size, (f0_length, option.fft_size // 2 + 1)


def d4c(x, fs, temporal_positions, f0,
        threshold=0.85, f0_floor=DEFAULT_F0_FLOOR, fft_size=None, **dummy):
    '''Aperiodicity estimation by D4C

    Args:
        x (POINTER(c_double)): Input waveform
        fs (int): a
        temporal_positions (POINTER(c_double)): Temporal positions
        f0 (POINTER(c_double)): Extracted F0
        threshold (double, optional): To determine frame is unvoice or not
                            (high value is tending to regard as unvoiced)
        f0_floor (double, optional): To determine fft_size
        fft_size (double, optional): When fft_size is not set, determined by fs and default f0_floor

    Returns:
        POINTER(POINTER(c_double)): Aperiodicity
        Tuple(int, int): Aperiodicity's shape "(f0_length, fft_size // 2 + 1)"
    '''

    option = structures.D4COption()

    apidefinitions._InitializeD4COption(option)

    option.threshold = threshold
    if fft_size is None:
        tmp_fft_size = get_fft_size(fs, f0_floor)
    else:
        tmp_fft_size = fft_size

    f0_length = get_f0_length(f0)

    tmp_2d_array = [[0 for i in range(tmp_fft_size // 2 + 1)] for  o in range(f0_length)]
    aperiodicity = utils.cast_2d_list_to_2d_pointer(tmp_2d_array, ctypes.c_double)

    apidefinitions._D4C(x, len(list(x)), fs, temporal_positions,
                        f0, f0_length, tmp_fft_size, option,
                        aperiodicity)

    return aperiodicity, tmp_fft_size, (f0_length, tmp_fft_size // 2 + 1)


def synthesis(f0, spectrogram, aperiodicity, fs, frame_period=DEFAULT_FRAME_PERIOD, 
              f0_floor=DEFAULT_F0_FLOOR, fft_size=None):
    '''WORLD synthesis

    Args:
        f0 (POINTER(c_double)): F0
        spectrogram (POINTER(POINTER(c_double))): Spectral envelope
        aperiodicity (POINTER(POINTER(c_double))): Aperiodicity
        fs (int): Sampling frequency [Hz]
        frame_period (double, optional): Frame shift [ms]
        f0_floor (double, optional): To determine fft_size
        fft_size (int, optional): FFT size used by CheapTrick and Aperiodicity

    Returns:
        POINTER(c_double): Output waveform
        int: Output waveform length

    Notice:
        When FFT size is not set, it's determined by fs and f0_floor.
        Additionaly f0_floor is not set, used DEFAULT_F0_FLOOR(71.0).
    '''

    f0_length = get_f0_length(f0)
    y_length = int(f0_length * 5.0 * fs // 1000) + 1
    y = (ctypes.c_double * y_length)()

    if fft_size is None:
        tmp_fft_size = get_fft_size(fs, f0_floor)
    else:
        tmp_fft_size = fft_size

    apidefinitions._Synthesis(f0, f0_length,
                              spectrogram, aperiodicity,
                              tmp_fft_size, frame_period, fs,
                              y_length, y)

    return y, y_length


def get_f0_length(f0):
    '''Get non Python list F0's length

    Args:
        f0 (POINTER(c_double)): F0

    Returns:
        int: F0 length
    '''

    return len(list(f0))


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
        x (POINTER(c_double)): Input waveform
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
        POINTER(c_double): F0
        POINTER(POINTER(c_double)): Spectral envelope
        POINTER(POINTER(c_double)): Aperiodicity
        int: FFT size
        Tuple(int, int): Parameter's rank "(f0_length, fft_size // 2 + 1)"
    '''

    if parameters.get('Dio') is True:
        base_f0, time_axis, _ = dio(x, fs, **parameters)
    else:
        base_f0, time_axis, _ = harvest(x, fs, **parameters)
    if parameters.get('StoneMask') is True:
        f0 = stone_mask(x, base_f0, fs, time_axis)
    else:
        f0 = base_f0

    sp, sp_fft, sp_size = cheap_trick(x, fs, time_axis, f0, **parameters)
    ap, ap_fft, _ = d4c(x, fs, time_axis, f0, **parameters)

    if sp_fft != ap_fft:
        raise Exception('FFT size is invalid, you should check parameters')

    return f0, sp, ap, sp_fft, sp_size


def code_spectral_envelope(spectrogram, fs, f0_length, number_of_dimensions, fft_size):
    '''Compress spectral envelope's dimension

    Args:
        spectrogram (POINTER(POINTER(c_double))): Spectral envelope
        fs (int): Sampling frequency [Hz]
        f0_length (int): Rank of spectrogram 1d
        number_of_dimensions (int): Number of compressed spectral envelope's dimension
        fft_size (int): FFT size

    Returns:
        POINTER(POINTER(c_double)): compressed spectral envelope
    '''

    tmp_2d_array = [[0 for i in range(number_of_dimensions)] for  o in range(f0_length)]
    coded_spectrogram = utils.cast_2d_list_to_2d_pointer(tmp_2d_array, ctypes.c_double)

    apidefinitions._CodeSpectralEnvelope(spectrogram, f0_length, fs, fft_size,
                                         number_of_dimensions, coded_spectrogram)

    return code_spectral_envelope


def decode_spectral_envelope(coded_spectral_envelope, fs, f0_length,
                             number_of_dimensions, fft_size):
    '''Restore compressed spectral envelope's dimension

    Args:
        coded_spectral_envelope (POINTER(POINTER(c_double))): Coded spectral envelope
        fs (int): Sampling frequency [Hz]
        f0_length (int): Rank of spectrogram 1d
        number_of_dimensions (int): Number of compressed spectral envelope's dimension
        fft_size (int): FFT size

    Returns:
        POINTER(POINTER(c_double)): Spectral envelope
    '''

    tmp_2d_array = [[0 for i in range(number_of_dimensions)] for  o in range(f0_length)]
    spectrogram = utils.cast_2d_list_to_2d_pointer(tmp_2d_array, ctypes.c_double)

    apidefinitions._DecodeSpectralEnvelope(coded_spectral_envelope, f0_length, fs,
                                           fft_size, number_of_dimensions, spectrogram)

    return spectrogram


def get_codec_aperiodicity_num(fs):
    '''Calculate dimension needed to code aperiodicity

    Args:
        fs (int): Sampling frequency [Hz]

    Returns:
        int: Required dimension
    '''

    return apidefinitions._GetNumberOfAperiodicities(fs)


def code_aperiodicity(aperiodicity, fs, f0_length, fft_size):
    '''Compress aperiodicity's dimension

    Args:
        aperiodicity (POINTER(POINTER(c_double))): Aperiodicity
        fs (int): Sampling frequency [Hz]
        f0_length (int): Rank of aperiodicity 1d
        fft_size (int): FFT size

    Returns:
        POINTER(POINTER(c_double)): compressed aperiodicity

    Notice:
        You can get compressed apeiodicity's rank via `get_codec_aperiodicity` method
    '''

    tmp_2d_array = [[0 for i in range(get_codec_aperiodicity_num(fs))] for  o in range(f0_length)]
    coded_aperiodicity = utils.cast_2d_list_to_2d_pointer(tmp_2d_array, ctypes.c_double)

    apidefinitions._CodeAperiodicity(aperiodicity, f0_length, fs, fft_size,
                                     coded_aperiodicity)

    return code_aperiodicity


def decode_aperiodicity(coded_aperiodicity, fs, f0_length, fft_size):
    '''Restore compressed aperiodicity's dimension

    Args:
        coded_aperiodicity (POINTER(POINTER(c_double))): Coded aperiodicity
        fs (int): Sampling frequency [Hz]
        f0_length (int): Rank of aperiodicity 1d
        fft_size (int): FFT size

    Returns:
        POINTER(POINTER(c_double)): Aperiodicity
    '''

    tmp_2d_array = [[0 for i in range(get_codec_aperiodicity_num(fs))] for  o in range(f0_length)]
    aperiodicity = utils.cast_2d_list_to_2d_pointer(tmp_2d_array, ctypes.c_double)

    apidefinitions._DecodeAperiodicity(coded_aperiodicity, f0_length, fs,
                                       fft_size, aperiodicity)

    return aperiodicity
