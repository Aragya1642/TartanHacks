import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100 # Sampling Rate
duration = 5 # Duration of recording

# Set the defaults for sounddevice module
sd.default.samplerate = fs
sd.default.channels = 2

# Perform recording and save as a wav file
myRecording = sd.rec(int(duration * fs))
sd.wait()
write('output.wav', fs, myRecording)
