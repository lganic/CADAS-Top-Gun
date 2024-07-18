
# Run dat V
# pip install sounddevice numpy scipy

# Still working on this! Not yet finished!

import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import threading
import queue
import soundfile as sf
import time
import os

# Global flag to control recording
is_recording = False

def start_recording(filename, device, duration=None):
    global is_recording
    is_recording = True

    def callback(indata, frames, time, status):
        if status:
            print(status)
        q.put(indata.copy())

    samplerate = 44100  # Sample rate
    q = queue.Queue()

    if os.path.exists(filename):
        os.remove(filename) # Because soundfile is dumb and throw error if not

    with sf.SoundFile(filename, mode='x', samplerate=samplerate, channels=1) as file:
        with sd.InputStream(samplerate=samplerate, device=device, channels=1, callback=callback):
            print("Recording started")
            while is_recording:
                file.write(q.get())


def stop_recording():
    global is_recording
    is_recording = False
    print("Recording stopped")

if __name__ == "__main__":
    # Print all devices to identify the correct one
    print(sd.query_devices())

    # Get the default output device
    default_output_device = sd.default.device[1]
    print(f"Default output device: {default_output_device}")

    filename = 'output.wav'
    
    # Start recording in a separate thread
    recording_thread = threading.Thread(target=start_recording, args=(filename, 41))
    recording_thread.start()
    
    # Record for 10 seconds (example)
    time.sleep(10)
    stop_recording()
    
    # Wait for the recording thread to finish
    recording_thread.join()