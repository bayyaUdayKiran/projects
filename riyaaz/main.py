from time import sleep
from time import time
import os
import random
import pyaudio
import numpy as np

def check_note():
  

    # Define constants
    CHUNK = 1024  # The number of frames per buffer
    FORMAT = pyaudio.paInt16  # Sample size and format
    CHANNELS = 1  # Mono sound
    RATE = 44100  # Sampling frequency (Hz)
    RECORD_SECONDS = 5  # Duration of recording (s)

    # Initialize PyAudio object
    audio = pyaudio.PyAudio()

    # Open audio stream
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE,
            input=True, frames_per_buffer=CHUNK)

    print("Play...")

    # Initialize variables
    frames = []
    num_frames = int(RATE / CHUNK * RECORD_SECONDS)

    # Loop over frames and append them to buffer
    for i in range(num_frames):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Note detection complete...")

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Concatenate recorded frames
    recorded_audio = b''.join(frames)

    # Convert byte data to numpy array
    audio_array = np.frombuffer(recorded_audio, dtype=np.int16)

    # Calculate Fourier Transform and frequency domain
    fft = np.fft.fft(audio_array)
    freq = np.fft.fftfreq(len(audio_array), d=1.0/RATE)

    # Find the frequency with the highest amplitude
    freq_peak = freq[np.argmax(np.abs(fft))]

    returnable = "{:.2f} Hz".format(abs(freq_peak))
    return returnable


if __name__ == "__main__":
    start = time()
    end = 1800
    swaras = ["Shadjam[Sa]", "Rishabham[Re]", "Gandharam[Ga]", "Madhyamam[Ma]", "Panchamam[Pa]", "Dhaivatam[Da]", "Nishadam[Ni]", "Taar Shadjam[Sa`]", "Taar Panchamam[Pa`]", "Taar Dhaivatam[Da`]", "Taar Nishadam[Ni`]" ]
    while True:
        if(time()-start > end):
            break
        note = random.randrange(1, 11)
        swara = swaras[note-1]
        print(swara)
        print(check_note())
        sleep(18)
        os.system('cls')

    
