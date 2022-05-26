# Dont-you-lecture-me-automation
A module to automate making music with the dont you lecture me with your 30 dollar website

I might update this later


# How to use:
Generate.py will automatically generate a module with every sound

use `import system` to use the module, all of the functions have a generate_<SOUNDNAME> or generate_<FUNCTION>_system if its a modifier

everything ill be written to a generated.txt file that can be directly loaded into the site
  
  
# Code samples:
  
```py
import system
import librosa

print("[ * ] Loading audio file.")

data, sr = librosa.load('audio.wav', sr=96)

print("[ * ] Loaded audio file.")

system.generate_speed_system(6080)

print("[ * ] Initialized system.")
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
```
```py
import system
import numpy as np

system.generate_speed_system(120)

print("[ * ] Initialized system.")

time        = np.arange(0, 2, 0.01)
amplitude   = np.sin(time)

print("[ + ] Generating sequence file.")

for y in amplitude:
    dat = round(y*50)

    if dat == 0:
        system.generate_no(0)
        continue
    
    system.generate_BABA(dat)

print("[ ! ] Sequence file generated.")

system.finalize()
```
