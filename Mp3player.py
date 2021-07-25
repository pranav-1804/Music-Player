from tkinter import *
from tkinter import filedialog
import pygame
from pygame import *
import os
import tkinter.ttk as ttk

window=Tk()
window.title('Music Player')
window.geometry("400x900")

pygame.mixer.init()

track=StringVar()
song_dir = []
i = 0

def play_song():
    global i
    song = song_box.get(ACTIVE)
    i = song_box.get(0, END).index(song)
    pygame.mixer.music.load(str(song_dir[i]))
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.play(0)
    track.set(song_box.get(ACTIVE))

def add_to_list():
    song = filedialog.askopenfilename(filetypes=(("mp3 Files", "*.mp3"),))
    song_dir.insert(len(song_dir), song)
    song_name = os.path.basename(song)
    song_name = song_name.replace(".mp3", "")
    song_box.insert(END, song_name)

paused=False

def pause_song(is_paused):
    global paused
    paused=is_paused
    if paused==True:
        pygame.mixer.music.unpause()
        paused=False
    else:
        pygame.mixer.music.pause()
        paused=True


def stop_song():
    mixer.music.stop()


def next_song():
    global i
    next_song=song_box.curselection()
    next_song=next_song[0]+1
    song=song_box.get(next_song)
    i = (i + 1) % (len(song_dir))
    pygame.mixer.music.load(str(song_dir[i]))
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.play(loops=0)
    song_box.selection_clear(0,END)
    song_box.activate(next_song)
    song_box.selection_set(next_song,last=None)
    track.set(song_box.get(ACTIVE))


def prev_song():
    global i
    pre_song=song_box.curselection()
    pre_song=pre_song[0]-1
    song=song_box.get(pre_song)
    i=i-1
    i=i % len(song_dir)
    pygame.mixer.music.load(str(song_dir[i]))
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.play(loops=0)
    song_box.selection_clear(0,END)
    song_box.activate(pre_song)
    song_box.selection_set(pre_song,last=None)
    track.set(song_box.get(ACTIVE))


def slider(x):
    slider_label.config(text=int(myslider.get()))
    pass




label1 = Label(window, fg='Black', font=('Helvetica 12 bold italic',10), bg='ivory4',height=13,width=50)
label1.place(x=0, y=0)

# output = Text(window, wrap=WORD, width=60)
# output.place(x=0, y=0)


play=Label(window,text="Playlist",height=1,width=20,font=("times new roman",16,"bold"))
play.place(x=-80,y=320)

song_box= Listbox(window,bg='White', fg='blue',height=100,width=60,selectbackground='Blue',selectforeground="Black")
song_box.pack(pady=350)

name=Label(window,text="Now Playing",height=1,width=19,font=("times new roman",16,"bold"))
name.place(x=-50,y=215)
songtrack = Label(window,textvariable=track,height=1,width=60,bg="peachpuff",fg="IndianRed3",font=("times new roman",16,"bold"))
songtrack.place(x=-170,y=250)

btn_add = Button(window, text="Add To Playlist", command=add_to_list, height=1, width=30)
btn_add.place(x=90, y=20)
btn_play = Button(window, text='Play Song', height=1, width=30, command=play_song)
btn_play.place(x=90, y=50)
btn_pause = Button(window, text='Pause/Unpause', height=1, width=30, command=lambda :pause_song(paused))
btn_pause.place(x=90, y=80)
btn_stop = Button(window, text='Stop', height=1, width=30, command=stop_song)
btn_stop.place(x=90, y=110)
btn_previous = Button(window, text='Previous Song', height=1, width=30,command=prev_song)
btn_previous.place(x=90, y=140)
btn_next = Button(window, text='Next Song', height=1, width=30,command=next_song)
btn_next.place(x=90, y=170)


status_bar=Label(window,text='',bd=1,relief=GROOVE,anchor=END)
status_bar.place(x=250,y=320)

myslider=ttk.Scale(window,from_=0,to=100,orient=HORIZONTAL,value=0,command=slider,length=370)
myslider.place(x=12,y=290)

slider_label=Label(window,text='0')
slider_label.place(x=180,y=320)

window.mainloop( )