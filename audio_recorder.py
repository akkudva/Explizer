import pyaudio
import wave
import os
import lameenc

#define audio parameters
format = pyaudio.paInt16
channels=1
rate = 16000
chunk= 1024
record_sec = int(input("Insert record time in seconds:- "))
op_fn_wav = input("Enter file name:- ")+".wav"
op_fn_mp3= op_fn_wav.replace(".wav", ".mp3")

# initialize the PyAudio object
audio = pyaudio.PyAudio()

# open the microphone stream
stream = audio.open(format=format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk)

print("Recording...")

# initialize the buffer to store the recorded audio
frames = []

# record the audio from the microphone
for i in range(0, int(rate / chunk * record_sec)):
    data = stream.read(chunk)
    frames.append(data)

print("Finished recording.")

# stop and close the microphone stream
stream.stop_stream()
stream.close()
audio.terminate()

# save the recorded audio to a WAV file
wf = wave.open(op_fn_wav, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(audio.get_sample_size(format))
wf.setframerate(rate)
wf.writeframes(b''.join(frames))
wf.close()

# convert the WAV file to MP3 using lameenc
with open(op_fn_wav, 'rb') as wav_file:
    wav_data = wav_file.read()
    encoder = lameenc.Encoder()
    encoder.set_bit_rate(128)
    encoder.set_in_sample_rate(rate)
    encoder.set_channels(channels)
    encoder.set_quality(2)
    mp3_data = encoder.encode(wav_data)
    encoder.flush()
    
with open(op_fn_mp3, 'wb') as mp3_file:
    mp3_file.write(mp3_data)

# remove the temporary WAV file
os.remove(op_fn_wav)
