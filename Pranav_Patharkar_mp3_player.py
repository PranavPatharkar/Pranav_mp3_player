from tkinter import *
from tkinter import filedialog
from pathlib import Path
import tkinter as x
from pygame import mixer

root =Tk()
root.geometry("450x500")
root.resizable(0,0)
root.title("PROJECT - MP3 PLAYER")
playlist = []
playlist_path = []
y = -1
number=0
def browse():
    global playlist_path
    file = filedialog.askopenfilename(title='Select an mp3 file', filetypes=[('MP3 Files', ['.mp3'])])
    if file == '': return 0
    else:
        playlist_path.append(file)
        file_path = file
        location = Path(file_path)
        file_name_real = str(location.name)
        global playlist
        playlist.append(file_name_real)
        length = len(playlist)
        for i in playlist:
            if i == playlist[length-1]:
                display = x.Entry(root, width=80)
                display.insert(END,i )
                display.pack()
                break

def play_music():
    if len(playlist)==0:
        return 0
    else:
        global y
        y = 0
        mixer.init()
        mixer.music.load(playlist_path[y])
        mixer.music.play(0)
        print('Current y is ',y)
        queue_next()

def queue_next():
    if len(playlist)==0:
        return 0
    else:
        global y
        pos = mixer.music.get_pos()
        if int(pos) == -1:
            y += 1
            print('current y is:', y)
            mixer.music.load(playlist_path[y])
            mixer.music.play(0)
        root.after(1, queue_next)

def pause_resume():
    if len(playlist)==0: return 0
    else:
        mixer.init()
        if mixer.music.get_busy() == True:
          mixer.music.pause()
        else:
          mixer.music.unpause()

def play_next():
    if len(playlist)==0: return 0
    else:
        global y
        if y == len(playlist_path)-1:
            y=0
            mixer.music.load(playlist_path[y])
            mixer.music.play(0)
            queue_next()
        elif y < len(playlist_path)-1:
            y += 1
            mixer.music.load(playlist_path[y])
            mixer.music.play(0)
            queue_next()

def play_previous():
    if len(playlist)==0: return 0
    else:
        global y
        if y == 0:
            y=len(playlist)-1
            mixer.music.load(playlist_path[y])
            mixer.music.play(0)
            queue_next()
        elif y >0:
            y =y - 1
            mixer.music.load(playlist_path[y])
            mixer.music.play(0)
            queue_next()

Button(root, text = "Browse Files to add" , command = browse, width=30,bg ='ivory2').pack(pady= 5)
Button(root, text = "Play", command = play_music,width = 30,bg ='ivory2').pack(pady= 5)
Button(root, text = "Pause/Resume",command = pause_resume ,width = 30,bg ='ivory2').pack(pady= 5)
Button(root, text = "Next Song",command = play_next, width = 30,bg ='ivory2').pack(pady= 5)
Button(root, text = "Previous Song",command = play_previous, width = 30,bg ='ivory2').pack(pady= 5)

heading2 = Label(root, text = 'THE PLAYLIST ' , font ='arial 8 bold').pack(pady=12)

root.mainloop()