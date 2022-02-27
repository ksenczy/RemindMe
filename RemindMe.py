#Assignment:    Remind Me
#Group:         Wesley Blanco, Matt Lake, Minh Nguyen, Kayla Senczyszyn
#Due:           March 4th 2022
#Professor:     Dr. Chao
#
#
#TO DO LIST
#Matt Photo and Info Bottom Right of Home Screen
#Make the pop ups work
#Attempt to fix the Button sizes on the Menu screen


from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import os
from datetime import datetime

#declaring colors
orange = '#FD5000'
brown ='#4F2C1D'
#font
fontSettings = ("Times New Roman", 24)
eventFont = ("Times New Roman", 34)
timeFont = ("Times New Roman", 18)

#declaring the window
window = Tk()
window.title("Remind Me")
window.geometry('1920x1080')
window.configure(bg=brown)


#This will be where the window changes from Login to the Home Screen
def clickedLogin():
    #This if so we can show off a failed login
    if(passwordEntry.get() != "p"):
        failureLabel = Label(window,background = brown,foreground = "red", text="(!)Unable to sign in", font = ("Times New Roman", 25)).place(x=800, y=690)
    else:
        Homescreen()

#This function converts eventTime1 into hours, minutes and seconds from
#a passed Time Delta, which holds days, seconds and microseconds
def convertTD(eventTime1):
    days, seconds = eventTime1.days, eventTime1.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 60)
    return hours, minutes, seconds



#This is the function for the home screen
def Homescreen():
    #Setting up the window
    window.destroy()
    homeWindow = Tk()
    homeWindow.title("Remind Me")
    homeWindow.geometry('1920x1080')
    homeWindow.configure(bg=brown)

    #Setting up the generic Labels for the home screen

    #Setting a black bar up
    #there are six labels for this so we dont have to mess with the image size
    blackBar = Image.open(holder + "\Black Bar.png")
    newTemp = ImageTk.PhotoImage(blackBar)
    blackBarLabel1 = Label(homeWindow, image = newTemp, background = brown).place(x=450, y = 25)
    blackBarLabel2 = Label(homeWindow, image = newTemp, background = brown).place(x=580, y = 25)
    blackBarLabel3 = Label(homeWindow, image = newTemp, background = brown).place(x=760, y = 25)
    blackBarLabel4 = Label(homeWindow, image = newTemp, background = brown).place(x=940, y = 25)
    blackBarLabel5 = Label(homeWindow, image = newTemp, background = brown).place(x=1120, y = 25)
    blackBarLabel6 = Label(homeWindow, image = newTemp, background = brown).place(x=1300, y = 25)

    #Setting up words
    agendaLbl = Label(homeWindow, background = orange, text = "Agenda", font = ("Times New Roman", 30), width = 35, anchor = CENTER).place(x=580, y= 50)
    remindMeLbl = Label(homeWindow, background = brown, foreground = "white", text = "Remind Me", font =("Times New Roman", 14)).place(x=1,y=1)

    #Setting New BG Logo
    bgLogo2 = Image.open(holder + "\BG Logo2.png")
    temp = ImageTk.PhotoImage(bgLogo2)
    bgImagelabel2 = Label(homeWindow, image = temp, background = brown).place(x=1500, y=50)

    #Setting up Event Block dates
    marchFifteenth = Label(homeWindow, text= "March 15th 2022", background = brown, foreground = "white", font=fontSettings).place(x=825, y=150)
    marchTwentySecond = Label(homeWindow, text="March 22nd 2022", background = brown, foreground = "white", font=fontSettings).place(x=825, y = 350)
    aprilFourth = Label(homeWindow, text="April 17th 2022", background = brown, foreground = "white", font=fontSettings).place(x=830, y = 700)
    timeLeft1 = Label(homeWindow, text = "Time Left:", background = brown, foreground = "white", font = fontSettings).place(x=1120, y=150)
    timeLeft2 = Label(homeWindow, text = "Time Left:", background = brown, foreground = "white", font = fontSettings).place(x=1120, y=350)
    timeLeft3 = Label(homeWindow, text = "Time Left:", background = brown, foreground = "white", font = fontSettings).place(x=1120, y=700)

    #Setting up Done? and its checkboxes
    doneLabel = Label(homeWindow, text = "Done?", background = brown, foreground = "white", font = fontSettings).place(x=1375, y=150)
    #Declaring vars for the checkboxes to work
    chk1 = IntVar()
    chk2 = IntVar()
    chk3 = IntVar()
    chk4 = IntVar()
    chk5 = IntVar()
    chk6 = IntVar()
    chk7 = IntVar()
    #Actually making the checkbuttons
    doneCheckbox1 = Checkbutton(homeWindow, variable = chk1, offvalue = 0, onvalue = 1).place(x=1400, y=220)
    doneCheckbox2 = Checkbutton(homeWindow, variable = chk2, offvalue = 0, onvalue = 1).place(x=1400, y=290)
    doneCheckbox3 = Checkbutton(homeWindow, variable = chk3, offvalue = 0, onvalue = 1).place(x=1400, y=420)
    doneCheckbox4 = Checkbutton(homeWindow, variable = chk4, offvalue = 0, onvalue = 1).place(x=1400, y=490)
    doneCheckbox5 = Checkbutton(homeWindow, variable = chk5, offvalue = 0, onvalue = 1).place(x=1400, y=570)
    doneCheckbox6 = Checkbutton(homeWindow, variable = chk6, offvalue = 0, onvalue = 1).place(x=1400, y=640)
    doneCheckbox7 = Checkbutton(homeWindow, variable = chk7, offvalue = 0, onvalue = 1).place(x=1400, y=765)


    #Hardcoding Events Here as Labels
    #We are presenting On March 15th, and as such all events will occur on or after that date
    #The first two events will have massively longer sections, as they are working fully for time until event
    currentTime = datetime.now()
    eventTime1 = datetime(2022, 3, 15, 15, 30)
    eventTime2 = datetime(2022, 3, 15, 20, 0)

    #First Event
    eventTime1 = -(currentTime - eventTime1)
    hours, minutes, seconds = convertTD(eventTime1) #converting EventTime into usable info
    if(hours == 1):
        hourFix = "Hour"
    else:
        hourFix = "Hours"
    if(minutes == 1):
        minuteFix = "Minute"
    else:
        minuteFix = "Minutes"
    if(seconds == 1):
        secondFix = "Second"
    else:
        secondFix = "Seconds"
    firstEvent = Label(homeWindow, background = "red", text = "CS 4120", font=eventFont, width = 35).place(x=525, y= 200)
    hourLabel1 = Label(homeWindow, background = "red", text = hours, font = timeFont).place(x=1070, y= 200)
    hourLabel2 = Label(homeWindow, background = "red", text = hourFix, font = timeFont).place(x=1050, y=225)
    minuteLabel1 = Label(homeWindow, background = "red", text = minutes, font=timeFont).place(x=1155, y=200)
    minuteLabel2 = Label(homeWindow, background = "red", text = minuteFix, font = timeFont).place(x=1130, y=225)
    secondLabel1 = Label(homeWindow, background = "red", text = seconds, font=timeFont).place(x=1250, y=200)
    secondLabel2 = Label(homeWindow, background = "red", text = secondFix, font = timeFont).place(x=1225, y=225)


    #Second Event
    eventTime2 = -(currentTime - eventTime2)
    hours, minutes, seconds = convertTD(eventTime2) #converting EventTime into usable info
    if(hours == 1):
        hourFix = "Hour"
    else:
        hourFix = "Hours"
    if(minutes == 1):
        minuteFix = "Minute"
    else:
        minuteFix = "Minutes"
    if(seconds == 1):
        secondFix = "Second"
    else:
        secondFix = "Seconds"
    secondEvent = Label(homeWindow, background = "red", text = "HIST 3014 Essay", font=eventFont, width = 35).place(x=525, y=275)
    secondHourLabel1 = Label(homeWindow, background = "red", text = hours, font = timeFont).place(x=1070, y= 275)
    secondHourLabel2 = Label(homeWindow, background = "red", text = hourFix, font = timeFont).place(x=1050, y=300)
    secondMinuteLabel1 = Label(homeWindow, background = "red", text = minutes, font=timeFont).place(x=1155, y=275)
    secondMinuteLabel2 = Label(homeWindow, background = "red", text = minuteFix, font = timeFont).place(x=1130, y=300)
    secondSecondLabel1 = Label(homeWindow, background = "red", text = seconds, font=timeFont).place(x=1250, y=275)
    secondSecondLabel2 = Label(homeWindow, background = "red", text = secondFix, font = timeFont).place(x=1225, y=300)


    #Third, Fourth, Fifth, and Sixth Events
    thirdEvent = Label(homeWindow, background = "green", text = "CS 4120", font=eventFont, width = 35).place(x=525, y= 400)
    fourthEvent = Label(homeWindow, background = "green", text = "ACM Meeting", font=eventFont, width = 35).place(x=525, y= 475)
    fifthEvent = Label(homeWindow, background = "green", text = "SOC 3170 Exam", font=eventFont, width = 35).place(x=525, y= 550)
    sixthEvent = Label(homeWindow, background = "green", text = "CS 3060", font=eventFont, width = 35).place(x=525, y= 625)

    #Seventh Event
    seventhEvent = Label(homeWindow, background = "green", text = "Easter", font=eventFont, width = 35).place(x=525, y= 750)

    #Implimenting Hamburger Button
    hamburger = Image.open(holder + "\HB Button.png")
    hamburg = ImageTk.PhotoImage(hamburger)
    menuButton = Button(image = hamburg, command = lambda: menuExtended(homeWindow)).place(x=50,y=50)
    #These cover labels cover an ugly border that doesnt match the color scheme
    coverLabel1 = Label(text="This is stupid", background = brown, foreground = brown).place(x=50, y=40)
    coverLabel2 = Label(text="This is stupid", background = brown, foreground = brown).place(x=50, y=100)
    coverLabel3 = Label(text= "T", background = brown, foreground = brown, font = eventFont).place(x=100, y=55)
    coverLabel4 = Label(text= "T", background = brown, foreground = brown, font = eventFont).place(x=25, y=55)

    #again, this must be at the bottom of the Homescreen function to
    #make sure that things work
    #notably, photos dont work without this
    homeWindow.mainloop()


#This function builds the menu window, right into the side of the Home Screen
def menuExtended(homeWindow):
    #Setting Frame Style so that it can take a bg color
    s = Style()
    s.configure('My.TFrame', background=brown)

    #Setting up the frame
    menu=Frame(homeWindow, style='My.TFrame')
    menu.config()
    menu.place(x=0,y=0, width = 400, height = 1080)


    #Setting up Button images
    createEventImg = Image.open(holder + "\Create EventBtn.png")
    createEventImgAnchor = ImageTk.PhotoImage(createEventImg)
    deleteEventImg = Image.open(holder + "\Delete Event.png")
    deleteEventImgAnchor = ImageTk.PhotoImage(deleteEventImg)
    updateEventImg = Image.open(holder + "\TUpdate Event.png")
    updateEventImgAnchor = ImageTk.PhotoImage(updateEventImg)
    searchEventImg = Image.open(holder + "\Search Event.png")
    searchEventImgAnchor = ImageTk.PhotoImage(searchEventImg)
    shareEventImg = Image.open(holder + "\Share Event.png")
    shareEventImgAnchor = ImageTk.PhotoImage(shareEventImg)
    sharedWithEventImg = Image.open(holder + "\Shared With Me.png")
    sharedWithEventImgAnchor = ImageTk.PhotoImage(sharedWithEventImg)
    organizationsEventImg = Image.open(holder + "\Organizations.png")
    organizationsEventImgAnchor = ImageTk.PhotoImage(organizationsEventImg)
    holidaysEventImg = Image.open(holder + "\Holidays.png")
    holidaysEventImgAnchor = ImageTk.PhotoImage(holidaysEventImg)
    filtersEventImg = Image.open(holder + "\Filter.png")
    filtersEventImgAnchor = ImageTk.PhotoImage(filtersEventImg)
    settingsEventImg = Image.open(holder + "\Settings.png")
    settingsEventImgAnchor = ImageTk.PhotoImage(settingsEventImg)




    #Adding Buttons to the Frame for each menu option
    createEventBtn = Button(menu, image = createEventImgAnchor, command = lambda : createEvent(False, homeWindow), text = "Create Event").place(x=50, y=150)
    deleteEventBtn = Button(menu, image = deleteEventImgAnchor, command = deleteEvent, text = "Delete Event").place(x=50, y=190)
    updateEventBtn = Button(menu, image = updateEventImgAnchor, command = lambda : createEvent(True, homeWindow), text = "Update Event").place(x=50, y=230)
    searchEventBtn = Button(menu, image = searchEventImgAnchor, command = searchEvent, text = "Search").place(x=50, y=270)
    shareBtn = Button(menu, image = shareEventImgAnchor, command = shareEvent, text = "Share").place(x=50, y=310)
    sharedWithMeEventBtn = Button(menu, image = sharedWithEventImgAnchor, command = sharedWithMe, text = "Shared with me").place(x=50, y=350)
    organizationsBtn = Button(menu, image = organizationsEventImgAnchor, command = organizations, text = "Organizations").place(x=50, y=390)
    holidaysBtn = Button(menu, image = holidaysEventImgAnchor, command = holidays, text = "Holidays").place(x=50, y=430)
    filterBtn = Button(menu, image = filtersEventImgAnchor, command = filters, text = "Filter").place(x=50, y=470)
    settingsBtn = Button(menu, image = settingsEventImgAnchor, command = settings, text = "Settings").place(x=50, y=510)

    #Rebuilding the hamburger Button, clicking the hamburger button again destroys the frame and its contents
    hamburger = Image.open(holder + "\HB Button.png")
    hamburg = ImageTk.PhotoImage(hamburger)
    framedMenuButton = Button(menu, image = hamburg, command = lambda: menu.destroy()).place(x=50,y=50)
    #These cover labels cover an ugly border that doesnt match the color scheme
    coverLabel1 = Label(menu, text="This is stupid", background = brown, foreground = brown).place(x=50, y=40)
    coverLabel2 = Label(menu, text="This is stupid", background = brown, foreground = brown).place(x=50, y=100)
    coverLabel3 = Label(menu, text= "T", background = brown, foreground = brown, font = eventFont).place(x=100, y=55)
    coverLabel4 = Label(menu, text= "T", background = brown, foreground = brown, font = eventFont).place(x=25, y=55)

    #Once again, this has to be at the end of the function for
    #Image purposes
    homeWindow.mainloop()

#Function definition for Create Event pop up or Update Event
def createEvent(isUpdateFunction, homeWindow):

    #This is so we only have to use one function for both create and update
    if(isUpdateFunction):
        labelWords = "Update Event"
        searchEvent("U")
    else:
        labelWords = "Create Event"

    #Setting up the popup window
    popUp = Tk()
    popUp.title(labelWords)
    popUp.geometry('800x700')
    popUp.configure(bg=brown)

    #Setting up the top logo
    topLogo = Label(popUp, text = labelWords, font=eventFont, background = brown, foreground = orange).place(x=300, y=50)




    buttonImage = Image.open(holder + "\Press Button.png")
    buttonImageAnchor = ImageTk.PhotoImage(buttonImage)



#Function def for delete event pop up
def deleteEvent():
    garbage = 0

#function def for searching for an event
def searchEvent(whatDo):

    #For update event pop up
    if (whatDo == "U"):
        garbage = 0

    garbage = 0

#function def for sharing an event
def shareEvent():
    garbage = 0

#function def for shared with me events
def sharedWithMe():
    garbage = 0

#function def for Organizations search
def organizations():
    garbage = 0

#function Def for holiday settings
def holidays():
    garbage = 0

#function def for Filter settings
def filters():
    garbage = 0

#Function def for Settings pop up
def settings():
    garbage = 0

#Setting up the login Screen
#Image
holder = os.getcwd()
bgLogo1 = Image.open(holder + "\BG Logo.png")
idk = ImageTk.PhotoImage(bgLogo1)
bgImagelabel = Label(image = idk, background = brown).place(x=475,y=-220)

#Remind Me Text
RemindMe = Label(window,background = brown,foreground = orange,text="Remind Me", font = ("Times New Roman", 100)).place(x=650, y=500)

#Username and Password Text and Buttons
userNameLabel = Label(window,background = brown,foreground = orange, text="Username:", font = fontSettings).place(x=800, y=750)
passwordLabel = Label(window,background = brown,foreground = orange, text="Password:", font = fontSettings).place(x=800, y=800)
userNameEntry = Entry(window).place(x=950, y=761)
passwordEntry = Entry(window, show="*")
passwordEntry.place(x=950, y=811)

#Login Button
loginBtnCell = Button(window, text="Login", command=clickedLogin,width = 20).place(x = 875, y = 900)

#Version Text
Version = Label(window,background = brown,foreground = orange,text="Version 1.0.0", font = ("Times New Roman", 14)).place(x=1800, y=1052)


#This keeps the window open for the application
#must always be at the bottom of the file
window.mainloop()
