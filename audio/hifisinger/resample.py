import os
import librosa
import soundfile as sf
from tqdm import tqdm

# define high parameters
out_samprate = 48000
read_dir = "Baseline-24k"
write_dir = "Baseline-24k-up_"

# define mkdir
def make_sure_path_exist(path):
    if not os.path.exists(path):
        os.makedirs(path)
make_sure_path_exist(write_dir)

# read dir
wave_files = os.listdir(read_dir)
wave_files.sort()

for wave_file in tqdm(wave_files):
    # read each file
    wave, sr = librosa.load(os.path.join(read_dir, wave_file), sr=None)
    resample_wave = librosa.resample(wave, sr, out_samprate)

    # write
    resample_wave_file = os.path.join(os.path.join(write_dir, wave_file.replace(".wav", "")+'.wav'))
    sf.write(resample_wave_file, resample_wave, out_samprate, subtype='PCM_16')

    # logging
    # print(f"{resample_wave_file}")

