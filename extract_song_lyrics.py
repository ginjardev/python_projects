from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import requests
from bs4 import BeautifulSoup
from googleapiclient.discovery import build


api_key = 'AIzaSyDJ7iFBaYNwecqtkgPggKNCL5WyC2K_xXQ'
cse_key = '256ad4492c10c48b5'

lyrics_app = Tk()
lyrics_app.geometry("500x300")
lyrics_app.title("Lyrics Extractor")
lyrics_app.config(bg="seagreen1")


song_label = Label(lyrics_app, text="Enter song name: ", bg="seagreen1")
song_label.grid(row=0, column=0, padx=10, pady=20)
song_entry = Entry(lyrics_app, width=40)
song_entry.grid(row=0, column=1)


def lyrics_extractor():
    global api_key, cse_key, song_entry
    song = song_entry.get()
    if len(song) <= 0:
        messagebox.showerror(message="Enter a song name")
        return
    else:
        lyric_object = build("customsearch", "v1", developerKey = api_key).cse()

        result = lyric_object.list(q=song, cx=cse_key).execute()

        try:
            first_value = next(iter(result["items"]))
        except: 
            messagebox.showwarning(message="Lyrics for " + " were not found")
            return
        result = requests.get(first_value["link"])
        soup_lyrics = BeautifulSoup(result.content, "html.parser")


        if("genius" in first_value["link"]):
            lyrics = soup_lyrics.find("div", {"id":"lyrics-root"})
        elif "azlyrics" in first_value["link"]:
            lyrics = soup_lyrics.find("div", {"class": '', "id":""})

        try:
            display_lyrics = scrolledtext.ScrolledText(lyrics_app, width = 60, height=10, font=("Ubuntu Mono",10), bd=0, bg="seagreen3")
            display_lyrics.insert("1.0",lyrics.text)
            display_lyrics.config(state=DISABLED)
            display_lyrics.grid(row=2, column=0, columnspan=3)
        except UnboundLocalError as e:
            messagebox.showwarning(message="Lyrics for " + song_entry.get() + " were not found")
            return


get_lyrics_button = Button(lyrics_app, text="Get Lyrics", command=lyrics_extractor)
get_lyrics_button.grid(row=1, columnspan=2,pady=20)

lyrics_app.mainloop()