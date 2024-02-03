import sounddevice as sd
import scipy.io.wavfile as wav
from scipy.io.wavfile import write

import numpy as np
from matplotlib import pyplot as plt
from scipy.fft import fft, fftfreq
import json

fs = 44100 # Sampling Rate
duration = 10 # Duration of recording
NOTES_MAP = json.load(open("notes_map.json"))

# Set the defaults for sounddevice module
sd.default.samplerate = fs
sd.default.channels = 2

# Perform recording and save as a wav file
# myRecording = sd.rec(int(duration * fs))
# sd.wait()
# write('output.wav', fs, myRecording)

# Open the wav file and extract data
wavLocation = "output.wav"
wav_file = open(wavLocation, "rb")
Sample_RATE, data = wav.read(wav_file)

# Plot my soundwave
t = 1 * np.arange(Sample_RATE * duration)

# Calculate the fourier transform of the sound wave
yf = fft(data[:Sample_RATE * duration])
xf = fftfreq(Sample_RATE * duration, 1 / Sample_RATE)

# 2 different techniques to try for sorting
#method 1
#In[data.length]: for xf, yf in od.items(): print(xf,yf)
#method 2
#dict(sorted(yf))


# # Map the frequencies to piano keys
# y = np.abs(yf)
# d = {}
# for i in range(0, len(y)):
#   if xf[i] > 0:
#     d[f"{xf[i]}"] = y[i]

# frequencies = []
# for key in d:
#    frequencies.append(d[key])

#   #Sort the Array
#    for i in range(len(frequencies)):
#      frequencies[i] = np.sort(frequencies[i])

# #Check if element is true
# #requencies.sort(frequencies)
# pitch = any(np.any(freq)for freq in frequencies)
# print(frequencies)

# # # Sort the dict so highest frequencies are at the top
# # d = sorted(d, key=d.get, reverse=True)

# # Get the top 10 notes
# bucket = []
# for i in d:
#   if len(bucket) == 10:
#     break
#   i = round(float(i))
#   if i not in bucket:
#     bucket.append(i)

# # Map to notes
# notes = []
# for i in bucket:
#   for note in NOTES_MAP:
#     note_freq = NOTES_MAP[note]

#     l_r = i - 4
#     h_r = i + 4
#     if l_r < note_freq and h_r > note_freq:
#       notes.append(note)
#       break

# print(list(set(notes)))
