import system, numpy as np
import librosa

print("[ * ] Loading audio file.")

data, sr = librosa.load('improvement.wav', sr=96)

print("[ * ] Loaded audio file.")

system.generate_speed_system(6080)

print("[ * ] Initialized system.")

time        = np.arange(0, 3, 0.01)
amplitude   = np.sin(time)

print("[ + ] Generating sequence file.")

for y in data:
    dat = round(y*500)
    if abs(dat) < 5:
        system.generate_no(0)
        continue

    if dat == 0:
        system.generate_no(0)
        continue
    
    system.generate_BABA(dat)

print("[ ! ] Sequence file generated.")

system.finalize()