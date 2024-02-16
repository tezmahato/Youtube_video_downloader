import tkinter
import customtkinter
from pytube import YouTube


def startDownload():
    ytlink = link.get()
    ytobject = YouTube(ytlink)
    video = ytobject.streams.get_highest_resolution()
    video.download()
    print("Download completed")


# system Setting
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Our app frame
app = customtkinter.CTk()
app.geometry("720*480")
app.title("YouTube Downloader")
# Adding UI Elements

title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)

# link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Download Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

# Run app
app.mainloop()
