from world4py.native import apis, tools, structures


x, fs, nbit = tools.get_wave_parameters('./sample.wav')
param = {
    # 'Dio': True,
    # 'StoneMask': True,
    'threshold': 0.3,
    'frame_period': 5.0,
}

f0, sp, ap, fft_size, array_size = apis.extract_all_from_waveform(x, fs, param)
y, _ = apis.synthesis(f0, sp, ap, fs, fft_size=fft_size)

tools.write_wav_file('./sample_syn.wav', y, fs, nbit)
