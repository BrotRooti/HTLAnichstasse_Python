'''
multible downloader
Phillip
11.6.22
'''

import os
import tkinter.ttk

from pytube import YouTube
from tkinter import simpledialog, messagebox, filedialog
from tkinter import *

DEBUG = False


class MyApp(Frame):
    def __init__(self, master):
        super().__init__(master)
        # self.pack(fill=BOTH, expand=True)
        master.geometry("200x200")
        # frame
        self.f1 = Frame(master=master)
        self.f1.pack(fill=BOTH, expand=True)
        self.create_buttons()
        # make the grid layout expand
        for x in range(2):
            self.f1.columnconfigure(x, weight=1)
            self.f1.rowconfigure(x, weight=1)
        # make the grid layout expand


    def create_buttons(self):
        b1 = Button(master=self.f1, text="YouTube Downloader", bg="red",
                    command=lambda: [self.youtube_chooser(), b1.destroy(),
                                     b2.destroy(), b3.destroy(), b4.destroy()])

        b2 = Button(master=self.f1, text="Spotify Downloader", bg="green",
                    command=lambda: [self.spotify_download(), b1.destroy(),
                                     b2.destroy(), b3.destroy(), b4.destroy()])

        b3 = Button(master=self.f1, text="Soundcloud Downloader", bg="orange",
                    command=lambda: [self.soundcloud_download(), b1.destroy(),
                                     b2.destroy(), b3.destroy(), b4.destroy()])

        b4 = Button(master=self.f1, text="1/1", bg="black",
                    command=lambda: [self.Placeholder_download(), b1.destroy(),
                                     b2.destroy(), b3.destroy(), b4.destroy()])

        b1.grid(row=0, column=0, sticky=N + S + E + W)
        b2.grid(row=0, column=1, sticky=N + S + E + W)
        b3.grid(row=1, column=0, sticky=N + S + E + W)
        b4.grid(row=1, column=1, sticky=N + S + E + W)
        # button alignment (b1=YT, b2=Spotify, b3= Soundcloud, b4= Placeholder)

    def youtube_chooser(self):
        if DEBUG:
            print("youtube chooser")

        # asks the user if he wants to download the video in mp4 or mp3 using buttons

        empty_button = Button(master=self.f1, text="", bg="white", )
        mp4 = Button(master=self.f1, text="Download the whole video", bg="red",
                     command=lambda: [self.youtube_download_mp4(), mp4.destroy(), mp3.destroy(),
                                      empty_button.destroy(), return_button.destroy()])
        mp3 = Button(master=self.f1, text="Download only the audio", bg="purple",
                     command=lambda: [self.youtube_download_mp3(), mp4.destroy(), mp3.destroy(),
                                      empty_button.destroy(), return_button.destroy()])
        return_button = Button(master=self.f1, text="Return", bg="green",
                               command=lambda: [self.create_buttons(), mp4.destroy(), mp3.destroy(),
                                                empty_button.destroy(), return_button.destroy()])


        mp3.grid(row=0, column=1, sticky=N + S + E + W)
        mp4.grid(row=0, column=0, sticky=N + S + E + W)
        return_button.grid(row=1, column=1, sticky=N + S + E + W)
        empty_button.grid(row=1, column=0, sticky=N + S + E + W)

    def youtube_download_mp4(self):
        if DEBUG:
            print("mp4")

        while True:
            try:
                url = simpledialog.askstring(title="Youtube Downloader", prompt="Bitte geben sie den Video Link ein.")
                yt = YouTube(url)
                # ask for the video url and looks it up in the youtube database
            except:
                messagebox.showinfo(title="Youtube Downloader", message="Bitte einen gültigen Link eingeben")
                continue

            path = filedialog.askdirectory(title="Youtube Downloader")
            # asks the user for the path where the video should be saved

            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            stream.download(output_path=path, skip_existing=False)
            # caches the file and downloads it

            messagebox.showinfo(title="Youtube Downloader", message="Download abgeschlossen")
            # shows a success message
            self.youtube_chooser()
            break

    def youtube_download_mp3(self):
        if DEBUG:
            print("mp3")

        while True:
            try:
                url = simpledialog.askstring(title="Youtube Downloader", prompt="Bitte geben sie den Video Link ein.")
                yt = YouTube(url)
                # ask for the video url and looks it up in the youtube database
            except:
                messagebox.showinfo(title="Youtube Downloader", message="Bitte einen gültigen Link eingeben")
                continue

            path = filedialog.askdirectory(title="Youtube Downloader")
            # asks the user for the path where the video should be saved

            stream = yt.streams.get_audio_only()
            file_name = stream.download(output_path=path, skip_existing=False)
            # caches the file and downloads it

            base, ext = os.path.splitext(file_name)
            try:
                new_file = base + ".mp3"
                os.rename(file_name, new_file)
                # renames the file to .mp3
            except:
                messagebox.showinfo(title="Youtube Downloader", message="Datei existiert bereits")
                break

            messagebox.showinfo(title="Youtube Downloader", message="Download abgeschlossen")
            # shows a success message
            self.youtube_chooser
            break

    def spotify_download(self):
        if DEBUG:
            print("Spotify")

        messagebox.showinfo(title="Spotify Downloader", message="Diese Funktion ist im Moment nicht verfügbar")

        return_button = Button(master=self.f1, text="Return", bg="green",
                               command=lambda: [self.create_buttons(), return_button.destroy()])

        return_button.grid(row=1, column=1, sticky=N + S + E + W)

    def soundcloud_download(self):
        if DEBUG:
            print("soundcloud")

        messagebox.showinfo(title="Soundcloud Downloader", message="Diese Funktion ist im Moment nicht verfügbar")

        return_button = Button(master=self.f1, text="Return", bg="green",
                               command=lambda: [self.create_buttons(), return_button.destroy()])

        return_button.grid(row=1, column=1, sticky=N + S + E + W)

    def Placeholder_download(self):
        if DEBUG:
            print("Placeholder")

        messagebox.showinfo(title="Placeholder Downloader", message="Diese Funktion ist im Moment nicht verfügbar")

        return_button = Button(master=self.f1, text="Return", bg="green",
                               command=lambda: [self.create_buttons(), return_button.destroy()])

        return_button.grid(row=1, column=1, sticky=N + S + E + W)


tk_window = Tk()
tk_window.title("Utility Downloader")
app = MyApp(tk_window)
app.mainloop()
