#Assignment:    Remind Me
#Group:         Wesley Blanco, Matt Lake, Minh Nguyen, Kayla Senczyszyn
#Due:           March 4th 2022
#Professor:     Dr. Chao
#
#

#FD5000

from tkinter import *
from tkinter.ttk import *


#declaring the window
window = Tk()
window.title("Remind Me")
window.geometry('1920x1080')
window.configure(bg='#4F2C1D')



#This will be where the window changes to the Home Screen
def clickedLogin():
    update()


#Setting up the login Screen
#TODO: Figure out how to color the Labels and Button
#TODO: Set up the Remind Me Text, BGSU Logo
userNameLabel = Label(window, text="Username:").place(x=850, y=650)
passwordLabel = Label(window, text="Password:").place(x=850, y=700)
userNameEntry = Entry(window).place(x=950, y=650)
passwordEntry = Entry(window).place(x=950, y=700)
loginBtnCell = Button(window, text="Login", command=clickedLogin).place(x = 900, y = 900)

#This keeps the window open for the application
#must always be at the bottom of the file
window.mainloop()
