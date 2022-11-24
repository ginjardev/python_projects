from tkinter import *
from tkinter import messagebox
import threading
import queue
import sounddevice as sd
import soundfile as sf



def threading_rec(x):
    if x == 1:
        t1 = threading.Thread(target = record_audio)
        t1.start()
    elif x == 2:
        global recording 
        recording = False
        messagebox.showinfo(message="Recording finished")
    elif x == 3:
        if file_exits:
            data, fs = sf.read("trial.wav", dtype="float32")
            sd.play(data, fs)
            sd.wait()
        else:
            messagebox.showerror(message="Record something to play")

            
def callback(indata, frames, time, status):
    q.put(indata.copy())


def record_audio():
    global recording
    recording = True
    global file_exits

    messagebox.showinfo(message="Recording Audio. Speak into the mic")
    with sf.SoundFile("trial.wav", mode="w", samplerate=44100, channels=2) as file:
        with sd.InputStream(samplerate=44100, channels=2, callback=callback):
            while recording == True:
                file_exits = True
                file.write(q.get())

            
                

voice_rec = Tk()
voice_rec.geometry("360x200")
voice_rec.title("Voice Recorder")
voice_rec.config(bg="#107dc2")
q = queue.Queue()

recording = False
file_exits = False


title_label = Label(voice_rec, text="Voice Recorder", bg ="#107dc2").grid(row=0, column=0, columnspan=3)
record_btn = Button(voice_rec, text="Record Audio", command=lambda m=1: threading_rec(m))
stop_btn = Button(voice_rec, text="Stop Recording", command=lambda m=2: threading_rec(m))
play_btn = Button(voice_rec, text="Play Recording", command=lambda m=3: threading_rec(m))

record_btn.grid(row=1, column=1)
stop_btn.grid(row=1,column=0)
play_btn.grid(row=1, column=2)

voice_rec.mainloop()