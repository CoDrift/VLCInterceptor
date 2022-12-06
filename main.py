import vlc
from time import sleep
from tkinter import *
from tkinter import filedialog

# Get local file
localMedia = vlc.MediaPlayer()
networkMedia = vlc.MediaPlayer()
filepath = filedialog.askopenfilename(initialdir="C:\\Users",
                                          title="Open file okay?",
                                          filetypes= (("media","*.mp4"),
                                          ("all files","*.*")))

# Getting stream data
# streamLoc = str(input("Enter stream location: "))
# print(streamLoc)

# Network Player
Media = vlc.Media("mmsh://127.0.0.1:8080")
networkMedia.set_media(Media)
networkMedia.play()

# Starting the player
media = vlc.Media(filepath)
localMedia.set_media(media)
localMedia.play()
sleep(5)

networkMedia.audio_set_volume(0)
networkMedia.video_set_scale(0.1)
localMedia.set_position(0.5)
localMedia.audio_set_volume(1)

# Player Controls after this
while localMedia.is_playing():
     # sleep(2)
     print(networkMedia.get_position())
     print(localMedia.get_position())
     # localMedia.set_position(networkMedia.get_position())