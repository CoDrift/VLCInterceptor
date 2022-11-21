import vlc
from time import sleep
from tkinter import *
from tkinter import filedialog

# Get local file
media_player = vlc.MediaPlayer()
filepath = filedialog.askopenfilename(initialdir="C:\\Users",
                                          title="Open file okay?",
                                          filetypes= (("media","*.mp4"),
                                          ("all files","*.*")))

# Getting stream data
streamLoc = str(input("Enter stream location: "))
print(streamLoc)

# Starting the player
media = vlc.Media(filepath)
media_player.set_media(media)
media_player.play()
sleep(5)

# Player Controls after this
while media_player.is_playing():
     sleep(1)