#Assignment:    Remind Me
#Group:         Wesley Blanco, Matt Lake, Minh Nguyen, Kayla Senczyszyn
#Due:           March 4th 2022
#Professor:     Dr. Chao
#
#

#FD5000

from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import os

#declaring colors
orange = '#FD5000'
brown ='#4F2C1D'
#font
fontSettings = ("Times New Roman", 24)

#declaring the window
window = Tk()
window.title("Remind Me")
window.geometry('1920x1080')
window.configure(bg=brown)


#This will be where the window changes to the Home Screen
def clickedLogin():
    if(passwordEntry.get() != "Password"):
        failureLabel = Label(window,background = brown,foreground = "red", text="(!)Unable to sign in", font = ("Times New Roman", 25)).place(x=800, y=690)
    else:
        Homescreen()

def Homescreen():
    window.destroy()
    homeWindow = Tk()
    homeWindow.title("Remind Me")
    homeWindow.geometry('1920x1080')
    homeWindow.configure(bg=brown)



#Setting up the login Screen
#Image
holder = os.getcwd() + "\BG Logo.png"
bgLogo1 = Image.open(holder)
idk = ImageTk.PhotoImage(bgLogo1)
bgImagelabel = Label(image = idk, background = brown).place(x=475,y=-220)

#Remind Me Text
RemindMe = Label(window,background = brown,foreground = orange,text="Remind Me", font = ("Times New Roman", 100)).place(x=650, y=500)

#Username and Password Text and Buttons
userNameLabel = Label(window,background = brown,foreground = orange, text="Username:", font = fontSettings).place(x=800, y=750)
passwordLabel = Label(window,background = brown,foreground = orange, text="Password:", font = fontSettings).place(x=800, y=800)
userNameEntry = Entry(window).place(x=950, y=761)
passwordEntry = Entry(window)
passwordEntry.place(x=950, y=811)

#Login Button
loginBtnCell = Button(window, text="Login", command=clickedLogin,width = 20).place(x = 875, y = 900)

#Version Text
Version = Label(window,background = brown,foreground = orange,text="Version 1.0.0", font = ("Times New Roman", 14)).place(x=1800, y=1052)


#This keeps the window open for the application
#must always be at the bottom of the file
window.mainloop()
