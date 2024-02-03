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

curl https://api.audd.io/ \
    -F api_token='cc8076adf56f1a5978cf720f4787018e' \
    -F url='https://audd.tech/example.mp3' \
    -F return='apple_musiec,spotify'
