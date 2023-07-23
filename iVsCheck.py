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

# Designed and developed by @ios_euphoria
messagebox.showinfo("Info", "Please make sure your iDevice is connected in Diag or Normal mode.. Enjoy :)")

# frame settings
root = App.Tk()
frame = App.Frame(root, width="400", height="200")
frame.pack(fill=BOTH,expand=True)
#App.Entry(root).pack(fill='x')

# uses current directory to load the image file for the icon
root.iconphoto(False, App.PhotoImage(file='lib\settings.gif'))



PTYPE = ""
VER = ""

def detectDevice():
    global PTYPE, VER
    #Detect device info and save it to a txt file so we can read it later 
    os.system("lib\ideviceinfo -s > lib\detected.txt")

    #This reads the file we wrote above
    f = open("lib\detected.txt", "r")
    fileData = f.read()
    f.close()

    #We read data 
    if("ERROR:" in fileData):
        print("Device not found")
        detectLbl.config(text = "Device not found")
    else:
        #Now we find Product type
        ptypeStart = "ProductType: "
        ptypeEnd = "ProductVersion:"
        ptypeS = str(fileData)

        ptypeFoundData = ptypeS[ptypeS.find(ptypeStart)+len(ptypeEnd):ptypeS.rfind(ptypeEnd)]
        PTYPE = str(ptypeFoundData)

        #We find OS Version
        verStart = "ProductVersion: "
        verEnd = "ProductionSOC:"
        verS = str(fileData)

        verFoundData = verS[verS.find(verStart)+len(verStart):verS.rfind(verEnd)]
        VER = str(verFoundData)

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

root.title("iVsCheck v1.0")
frame.pack()
root.geometry("400x200")

root.resizable(False, False)

root.eval('tk::PlaceWindow . center')
root.mainloop()