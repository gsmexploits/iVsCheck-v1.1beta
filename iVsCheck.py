# Import system functions 
import os
import time
import re
import tkinter as App
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from subprocess import run
import subprocess
# load images in Tkinter python
from PIL import ImageTk, Image
# web
import webbrowser
# sounds
# from pygame import mixer

# First pop up
messagebox.showinfo("Info", "Please make sure your iDevice is connected in Diag or Normal mode.. Enjoy :)")

# frame settings
root = App.Tk()
frame = App.Frame(root, width="400", height="200")
frame.pack(fill=BOTH,expand=True)
#App.Entry(root).pack(fill='x')

# uses current directory to load the image file for the icon
root.iconphoto(False, App.PhotoImage(file='lib\settings.gif'))

def detectDevice():
    #Detect device info and save it to a txt file so we can read it later 
    os.system("lib\ideviceinfo -s -k ProductVersion > lib\detected.txt")
    #This reads the file we wrote above
    f = open("lib\detected.txt", "r")
    fileData = f.read()
    f.close()
    VER = str(fileData)

    if("ERROR:" in fileData):
        print("Device not found")
        detectLbl.config(text = "Device not found")
    else:
        #We output it with a popup
        detectLbl.config(text = "")
        messagebox.showinfo("Device Found", "OS Version : "+VER)
        os.system("del lib\detected.txt")


def callback(url):
   webbrowser.open_new_tab(url)

#Big title on the program 
mainText = Label(root, text="iVsCheck",font=('Calibri', 24))
mainText.place(x=5, y=5)

#The detect button 
detectBtn = App.Button(frame,
                       text = "Detect",
                       command = detectDevice,
                       state = "normal",
                       width = 15)
detectBtn.place(x=150, y=80)

detectLbl = App.Label(frame,
                      text = "")
detectLbl.place(x=160, y=110)

#Create a Label to display the link
link = Label(root, text="Made with ❤️by: @gsmexploits",font=('Helveticabold', 10), cursor="hand2")
link.place(x=190, y=170)
link.bind("<Button-1>", lambda e:
callback("https://youtube.com/@gsmexploits"))

root.title("iVsCheck v1.1 beta")
frame.pack()
root.geometry("400x200")

root.resizable(False, False)

root.eval('tk::PlaceWindow . center')
root.mainloop()