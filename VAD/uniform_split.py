import math

from pathlib import Path
from scipy.io import wavfile


file_name = 'aisvi'
in_audio = Path(__file__).parents[1] / 'example' / 'audios' / '16k' / f'{file_name}.wav'
samplerate, signal = wavfile.read(in_audio)
audio_len_sec = len(signal) / samplerate
out_lab = Path(__file__).parents[1] / 'example' / 'uniform' / f'{file_name}.lab'
num_uniform_splits = math.floor(audio_len_sec / 1.5)
uniform_splits = ['{:.3f} {:.3f} speech\n'.format(1.5 * i, 1.5 * (i+1)) for i in range(num_uniform_splits)]
with open(out_lab, 'w') as f:
    f.writelines(uniform_splits)

