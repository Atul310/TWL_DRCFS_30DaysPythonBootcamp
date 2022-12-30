import pyaudio ## importing module 
import wave 
## simple sound recorder importing modules 
audio =pyaudio.PyAudio()##Creating  audio object 
s= audio.open(format=pyaudio.paInt16,channels=1,rate=44000,input =True,frames_per_buffer=1024) ##setting format
frames=[] #creating empty list to store 
  
try:
    while True:
        data =s.read(1)
        frames.append(data) #3 appending




except KeyboardInterrupt: #pressing ctrl+C it will terminate recording
 pass

s.stop_stream()
s.close()
audio.terminate()
sound_file = wave.open("Recording.wav","wb") # writing by binary file
sound_file.setnchannels(1)
sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
sound_file.setframerate(44000)
sound_file.writeframes(b"".join(frames))
sound_file.close()