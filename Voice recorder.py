import sounddevice
from scipy.io.wavfile import write

fs=44100
second = int(input("Enter the Recording Time in second: "))
rec_file_name = str(input("Enter the Recording file name: "))
print("Recording.....\n")

record_voice = sounddevice.rec(int(second * fs), samplerate=fs, channels=2)
sounddevice.wait()
write(rec_file_name, fs, record_voice)
print("Voice Recording is Done. Please Check the recording file in folder.")